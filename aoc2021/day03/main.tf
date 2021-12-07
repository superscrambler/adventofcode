data "local_file" "input" {
    filename = "input"
}

# part 1
locals {
    diagnostic = split("\n", data.local_file.input.content)
    len = length(local.diagnostic[0])
    bits = [
        for i in range(local.len) : [
            for n in local.diagnostic : tonumber(substr(n, i, 1))
        ]
    ]
    gamma_bits = [
        for i in range(local.len) : sum(local.bits[i]) > length(local.diagnostic) / 2 ? 1 : 0
    ]
    gamma_rate = join("", [ for n in local.gamma_bits : tostring(n) ])
    epsilon_bits = [
        for n in local.gamma_bits : n == 0 ? 1 : 0
    ]
    epsilon_rate = join("", [ for n in local.epsilon_bits : tostring(n) ])
}

output "part1" {
    value = parseint(local.gamma_rate, 2) * parseint(local.epsilon_rate, 2)
}

# part 2
module "filter0" {
    source = "./filter"
    bit = 0
    oxy_input = local.diagnostic
    co2_input = local.diagnostic
}
module "filter1" {
    source = "./filter"
    bit = 1
    oxy_input = module.filter0.oxy_output
    co2_input = module.filter0.co2_output
}
module "filter2" {
    source = "./filter"
    bit = 2
    oxy_input = module.filter1.oxy_output
    co2_input = module.filter1.co2_output
}
module "filter3" {
    source = "./filter"
    bit = 3
    oxy_input = module.filter2.oxy_output
    co2_input = module.filter2.co2_output
}
module "filter4" {
    source = "./filter"
    bit = 4
    oxy_input = module.filter3.oxy_output
    co2_input = module.filter3.co2_output
}
module "filter5" {
    source = "./filter"
    bit = 5
    oxy_input = module.filter4.oxy_output
    co2_input = module.filter4.co2_output
}
module "filter6" {
    source = "./filter"
    bit = 6
    oxy_input = module.filter5.oxy_output
    co2_input = module.filter5.co2_output
}
module "filter7" {
    source = "./filter"
    bit = 7
    oxy_input = module.filter6.oxy_output
    co2_input = module.filter6.co2_output
}
module "filter8" {
    source = "./filter"
    bit = 8
    oxy_input = module.filter7.oxy_output
    co2_input = module.filter7.co2_output
}
module "filter9" {
    source = "./filter"
    bit = 9
    oxy_input = module.filter8.oxy_output
    co2_input = module.filter8.co2_output
}
module "filter10" {
    source = "./filter"
    bit = 10
    oxy_input = module.filter9.oxy_output
    co2_input = module.filter9.co2_output
}
module "filter11" {
    source = "./filter"
    bit = 11
    oxy_input = module.filter10.oxy_output
    co2_input = module.filter10.co2_output
}

output "part2" {
    value = parseint(module.filter11.oxy_output[0], 2) * parseint(module.filter11.co2_output[0], 2)
}