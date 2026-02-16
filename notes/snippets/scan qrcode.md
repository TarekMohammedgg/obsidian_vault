

package : `mobile_scanner: ^6.0.3`
```dart 
Future<void> _scanQRCode() async {
    setState(() {
      isScanning = true;
      scannerController = MobileScannerController();
    });

    await showDialog(
      context: context,
      builder: (context) => Dialog(
        child: Container(
          height: 400,
          padding: const EdgeInsets.all(16),
          child: Column(
            children: [
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Text(
                    'Scan Barcode',
                    style: Theme.of(context).textTheme.titleLarge,
                  ),
                  IconButton(
                    onPressed: () {
                      scannerController?.dispose();
                      Navigator.pop(context);
                    },
                    icon: const Icon(Icons.close),
                  ),
                ],
              ),
              const SizedBox(height: 16),
              Expanded(
                child: MobileScanner(
                  controller: scannerController,
                  onDetect: (capture) {
                    final List<Barcode> barcodes = capture.barcodes;
                    if (barcodes.isNotEmpty) {
                      final String? code = barcodes.first.rawValue;
                      if (code != null) {
                        setState(() {
                          barcodeController.text = code;
                        });
                        scannerController?.dispose();
                        Navigator.pop(context);
                        _showSuccessSnackBar('Barcode scanned: $code');
                      }
                    }
                  },
                ),
              ),
            ],
          ),
        ),
      ),
    );

    setState(() {
      isScanning = false;
    });
  }
```
