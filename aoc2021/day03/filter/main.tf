variable "bit"  { type = number }
variable "oxy_input" { type = list(string) }
variable "co2_input" { type = list(string) }

locals {
    len = length(var.oxy_input[0])
    oxy_bits = [ for n in var.oxy_input : tonumber(substr(n, var.bit, 1)) ]
    most_bit = sum(local.oxy_bits) >= length(var.oxy_input) / 2 ? 1 : 0
    co2_bits = [ for n in var.co2_input : tonumber(substr(n, var.bit, 1)) ]
    least_bit = sum(local.co2_bits) >= length(var.co2_input) / 2 ? 0 : 1
}

output "oxy_output" {
    value = length(var.oxy_input) == 1 ? var.oxy_input : [
        for n in var.oxy_input :
            n if tonumber(substr(n, var.bit, 1)) == local.most_bit
    ]
}
output "co2_output" {
    value = length(var.co2_input) == 1 ? var.co2_input : [
        for n in var.co2_input :
            n if tonumber(substr(n, var.bit, 1)) == local.least_bit
    ]
}