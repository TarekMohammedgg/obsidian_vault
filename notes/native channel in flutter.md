---
due_date: 2025-10-05
tags:
  - native_channel
related: "[[flutter]]"
---
طريقة او زي جسر بيخليني اقدر اتواصل مع كود مكتوب بـ Native Linguae زي Kotlin or Swift or Java ، بغرض التحطم في حاجة خاصة بالـ Platform الي عليها Android or iPhone or mac 

فيه انواع مختلفة من ال channels كل نوع بيختلف علي حسب بالهدف من التواصل 
`MethodChannel`
الغرض  الاساسي منه هو اني استدعي فانكشن بتعمل حاجه في ال Native و بترجعلي ال Result و خلاص علي كده 

`EventChannel`
الغرض منها هو اني بطلب حاجة زي Stream مثال علي الكلام ده لو انا عايز اعرف ال Sensor بتاع الجهاز، يعني بناءاً علي حركة الجهاز مثلا ابدأ اخاد Action عندي في التطبيق ، و ده بيتم استخدامه في ال Fit Tracker Applications . 
`BasicMethodChannel` 

==الفرق بينهم برده ايه ؟ ==
`MethodChannel` => Flutter to Native 

`EventChannel` => Native to Flutter (imagine it like Play Radio  )

`BasicMethodChannel` => Flutter <-> Native (like chat between flutter and native platform , imagine it like what's App chat)

## Examples 

### the code for get battery on kotlin  
```kotlin
package com.example.native_channel_tutorial

import android.os.Bundle
import android.content.Context
import android.os.BatteryManager
import io.flutter.embedding.android.FlutterActivity
import io.flutter.embedding.engine.FlutterEngine
import io.flutter.plugin.common.MethodChannel

class MainActivity : FlutterActivity() {
    private val CHANNEL = "Battery"

    override fun configureFlutterEngine(flutterEngine: FlutterEngine) {
        super.configureFlutterEngine(flutterEngine)

        MethodChannel(flutterEngine.dartExecutor.binaryMessenger, CHANNEL).setMethodCallHandler {
            call, result ->
            if (call.method == "getBatteryLevel") {
                val batteryLevel = getBatteryLevel()

                if (batteryLevel != -1) {
                    result.success(batteryLevel)
                } else {
                    result.error("UNAVAILABLE", "Battery level not available.", null)
                }
            } else {
                result.notImplemented()
            }
        }
    }

    private fun getBatteryLevel(): Int {
        val batteryManager = getSystemService(Context.BATTERY_SERVICE) as BatteryManager
        return batteryManager.getIntProperty(BatteryManager.BATTERY_PROPERTY_CAPACITY)
    }
}
```

### The code of the Sensor (Kotlin) 
```kotlin
package com.example.native_channel_tutorial

import android.content.Context
import android.hardware.Sensor
import android.hardware.SensorEvent
import android.hardware.SensorEventListener
import android.hardware.SensorManager
import io.flutter.embedding.android.FlutterActivity
import io.flutter.embedding.engine.FlutterEngine
import io.flutter.plugin.common.EventChannel

class MainActivity : FlutterActivity() {
    private val SENSOR_CHANNEL = "sensors"
    private var sensorManager: SensorManager? = null
    private var sensorEventListener: SensorEventListener? = null

    override fun configureFlutterEngine(flutterEngine: FlutterEngine) {
        super.configureFlutterEngine(flutterEngine)

        EventChannel(flutterEngine.dartExecutor.binaryMessenger, SENSOR_CHANNEL)
            .setStreamHandler(object : EventChannel.StreamHandler {
                override fun onListen(arguments: Any?, events: EventChannel.EventSink?) {
                    sensorManager = getSystemService(Context.SENSOR_SERVICE) as SensorManager
                    val sensor = sensorManager?.getDefaultSensor(Sensor.TYPE_ACCELEROMETER)

                    sensorEventListener = object : SensorEventListener {
                        override fun onSensorChanged(event: SensorEvent) {
                            val x = event.values[0]
                            val y = event.values[1]
                            val z = event.values[2]
                            // Send to Flutter
                            events?.success("x: $x, y: $y, z: $z")
                        }

                        override fun onAccuracyChanged(sensor: Sensor?, accuracy: Int) {}
                    }

                    sensorManager?.registerListener(
                        sensorEventListener,
                        sensor,
                        SensorManager.SENSOR_DELAY_NORMAL
                    )
                }

                override fun onCancel(arguments: Any?) {
                    sensorManager?.unregisterListener(sensorEventListener)
                }
            })
    }
}
```




