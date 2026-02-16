

## 📅 Open Tasks (Daily Notes)
> This list automatically pulls all unchecked tasks from your journals.

```dataview
task
from "journals/dailys"
where !completed
group by file.name
sort key desc
```
