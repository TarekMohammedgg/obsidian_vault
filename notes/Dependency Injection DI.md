#software #design_pattern 
related:: [[Archive/MOCS 1/flutter]]
هي عبارة عن [[Design Pattern]]  

is a specific implementation from [[Inversion of control IOC]]


بيحل مشكلة دلوقتي لما يكون عندك tightly coupling  ، يعني عندك اعتمادية ما بين ال two class يعني لو عدلت في واحد التاني هيسمع فيه التعديل . 

فكرة الحل بقي : هي بدل ما اعرف object في ال class التاني لأ انا كل الي هعمله اني هعرف ال object مثلا في ال main 

simple example for DI (constructor injection): 

```dart 
// bad scenario : 
class ApiClient {
void getData() {
print('Fetching data from internet');
}
}

class Repository {
final ApiClient apiClient = ApiClient(); // tightly coupled

void fetchData() {
apiclient.getData() ; 
}
}

void main() {
  Repository repository = Repository();
  repository.fetchData();
}

```

```dart 
// good scenario 
class ApiClient {
void getData() {
print('Fetching data from internet');
}
}

class Repository {
final ApiClient apiClient ;  //loose coupling 
Repository(this.apiClient) ; 
void fetchData() {
apiclient.getData() ; 
}
}

void main() {
ApiClient apiClient = ApiClient() ; 
Repository repository = Repository(apiClient);
repository.fetchData();
}

```


---
Types of DI : 
Constructor injection 
Setter injection 
بعمل inject بس بدل مافي ال constructor لا ، بعملها داخل ال setter و ده ممك يسبب مشاكل كتير من اكبرها اني ممكن انسي اصلا احط ال injection في اثناء استدعاء ال Repository مثلاً زائد ان الكود بقي مش احسن كـ readable و بقي  mutable  اني  بقيت اقدر اعدل في ال behavior في ال runtime . 
Method injection 
من ضمن العيوب بتاعته هي انه بيزود ال complexity 
