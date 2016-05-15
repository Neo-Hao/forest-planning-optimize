# Forest Planning Optimization using the Genetic Algorithm

This repo contains the implementation of the Genetic Algorithm (GA) on the Forest Planning problems. For the introduction to Forest Planning problem, see <a href="https://www.researchgate.net/profile/Walter_Potter/publication/225377320_Diagnosis_Configuration_Planning_and_Pathfinding_Experiments_in_Nature-Inspired_Optimization/links/54c7bc950cf22d626a3700b0.pdf">Potter, W. D., Drucker, E., Bettinger, P., Maier, F., Martin, M., Luper, D., ... & Hayes, C. (2009). Diagnosis, configuration, planning, and pathfinding: Experiments in nature-inspired optimization. <i>In Natural Intelligence for Scheduling, Planning and Packing Problems (pp. 267-294)</i>. Springer Berlin Heidelberg.</a>. For the report of this application, see <a href="#">here</a>.

## Files

1. fixedInput.py --- Get the input data for fitness calculation and verification
2. simpleGA.py --- Implementation of GA (<i>fitness calculation not included</i>)
3. fitnessMDF.py --- Fitness calculation and adjacency issue fix scheme
4. wrapperGA.py --- Combination of other essential elements of GA, generational fitness calculation and adjacency issue fix scheme

## Data

<i>Note: The source of data is <a href="http://cobweb.cs.uga.edu/~potter/" target="_blank">Dr. Potter</a> from University of Georgia</i>

1. West_73_units_adjacency.txt --- The adjacency table
2. West_73_units_volumes.txt --- The production volumes of each field on three time periods

## Testing

Keep the file structure. In python set your local working environment to the folder "ga-pso-mfd >>Genetic_Algorithm". Run wrapperGA.py firstly, then use the classes. An example is shown as the following:

```python
# assuming you have run wrapperGA.py
test = WrapperGa(100000, 1, 0.8, 0.02)
test.evolution()

# Check the results mentioned in the above paper and report
```

## Usage

If you have a customized fitness function, you can easily plug in your code to replace what is currently in <strong>FitnessCalc</strong> class.