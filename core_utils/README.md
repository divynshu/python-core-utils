# Python Core Utilities

## Why These Patterns Matter

This repository demonstrates **core Python patterns** that are used in professional codebases:

1. **Decorators** - Enhance function behavior dynamically, e.g., timing, retrying, logging.  
2. **Context Managers** - Ensure proper setup and cleanup of resources, e.g., files, timers.  
3. **Generators** - Produce values lazily, reducing memory usage for large or infinite sequences.  
4. **Type Hints** - Make code self-documenting and catch errors early with static analysis.  

Each utility in this package is small but demonstrates a **core pattern that improves code readability, efficiency, and safety**.  


# Python Core Utilities

## Why These Patterns Matter

This repository demonstrates **core Python patterns** used in professional codebases:

1. **Decorators** – Enhance function behavior dynamically (timing, retrying, logging)
2. **Context Managers** – Ensure proper setup and cleanup of resources
3. **Generators** – Produce values lazily to reduce memory usage
4. **Type Hints** – Improve readability and enable static analysis

Each utility is small but demonstrates a **core pattern that improves code readability, efficiency, and safety**.

---

## Imports

Each utility can be imported like this:

```python
from core_utils.decorators import timer, retry
from core_utils.context_managers import open_file, timer_cm
from core_utils.generators import fibonacci, evens
from core_utils.type_hints_examples import sum_numbers, printer

