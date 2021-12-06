data "local_file" "input" {
    filename = "input"
}

locals {
    measurements = split("\n", data.local_file.input.content)
    increased = [
        for i, m in slice(local.measurements, 1, length(local.measurements)) : m
        if local.measurements[i+1] > local.measurements[i]
    ]
    sliding_sums = [
        for i,m in slice(local.measurements, 0, length(local.measurements)-2) :
            local.measurements[i] + local.measurements[i+1] + local.measurements[i+2]
    ]
    sliding_increases = [
        for i,m in slice(local.sliding_sums, 1, length(local.sliding_sums)) : m
        if local.sliding_sums[i+1] > local.sliding_sums[i]
    ]
}

output "part1" {
    value = length(local.increased)
}
output "part2" {
    value = length(local.sliding_increases)
}