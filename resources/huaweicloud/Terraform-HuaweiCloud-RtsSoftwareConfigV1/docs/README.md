# Terraform::HuaweiCloud::RtsSoftwareConfigV1

Provides an RTS software config resource.

# Example Usage

 ```hcl
variable "config_name" {}

resource "huaweicloud_rts_software_config_v1" "myconfig" {
  name = "${var.config_name}"
}
 ```

# Argument Reference

The following arguments are supported:

* `name` - (Required) The name of the software configuration.

* `group` - (Optional) The namespace that groups this software configuration by when it is delivered to a server.

* `inputs` - (Optional) A list of software configuration inputs.

* `outputs` - (Optional) A list of software configuration outputs.

* `config` - (Optional) The software configuration code.

* `options` - (Optional) The software configuration options.


# Attributes Reference

In addition to all arguments above, the following attributes are exported:

* `id` - The id of the software config.
 
# Import

Software Config can be imported using the `config id`, e.g.
```
 $ terraform import huaweicloud_rts_software_config_v1 4779ab1c-7c1a-44b1-a02e-93dfc361b32d
```

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::HuaweiCloud::RtsSoftwareConfigV1",
    "Properties" : {
        "<a href="#config" title="Config">Config</a>" : <i>String</i>,
        "<a href="#group" title="Group">Group</a>" : <i>String</i>,
        "<a href="#inputvalues" title="InputValues">InputValues</a>" : <i>[ [ <a href="inputvalues.md">InputValues</a>, ... ], ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#options" title="Options">Options</a>" : <i>[ <a href="options.md">Options</a>, ... ]</i>,
        "<a href="#outputvalues" title="OutputValues">OutputValues</a>" : <i>[ [ <a href="outputvalues.md">OutputValues</a>, ... ], ... ]</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::HuaweiCloud::RtsSoftwareConfigV1
Properties:
    <a href="#config" title="Config">Config</a>: <i>String</i>
    <a href="#group" title="Group">Group</a>: <i>String</i>
    <a href="#inputvalues" title="InputValues">InputValues</a>: <i>
      - List of <a href="inputvalues.md">InputValues</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#options" title="Options">Options</a>: <i>
      - <a href="options.md">Options</a></i>
    <a href="#outputvalues" title="OutputValues">OutputValues</a>: <i>
      - List of <a href="outputvalues.md">OutputValues</a></i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Config

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Group

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InputValues

_Required_: No

_Type_: List of List of <a href="inputvalues.md">InputValues</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Options

_Required_: No

_Type_: List of <a href="options.md">Options</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutputValues

_Required_: No

_Type_: List of List of <a href="outputvalues.md">OutputValues</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

