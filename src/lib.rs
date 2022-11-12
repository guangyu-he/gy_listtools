use pyo3::prelude::*;
use itertools::Itertools;

#[pyfunction]
fn remove_duplicates(input: Vec<&str>) -> PyResult<Vec<&str>> {
    let output: Vec<_> = input.into_iter().unique().collect();
    Ok(output)
}

#[pyfunction]
fn remove_element_by_value(nums: Vec<&str>, item: &str) -> PyResult<Vec<String>> {
    let mut output: Vec<String> = vec![];

    match nums.is_empty() {
        true => return Ok(output),
        false => {
            for i in 0..nums.len() {
                if nums[i] == item {} else {
                    output.push(nums[i].to_string());
                }
            }
            Ok(output)
        }
    }
}

#[pyfunction]
fn remove_element_by_index(mut input: Vec<&str>, index: usize) -> PyResult<Vec<&str>> {
    match index >= input.len() {
        true => Ok(input),
        false => {
            input.remove(index);
            Ok(input)
        }
    }
}


/// A Python module implemented in Rust.
#[pymodule]
fn gy_listtools(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(remove_duplicates, m)?)?;
    m.add_function(wrap_pyfunction!(remove_element_by_value, m)?)?;
    m.add_function(wrap_pyfunction!(remove_element_by_index, m)?)?;
    Ok(())
}