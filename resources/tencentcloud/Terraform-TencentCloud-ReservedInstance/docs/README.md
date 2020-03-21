# Terraform::TencentCloud::ReservedInstance

Provides a reserved instance resource.

~> **NOTE:** Reserved instance cannot be deleted and updated. The reserved instance still exist which can be extracted by reserved_instances data source when reserved instance is destroied.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::ReservedInstance",
    "Properties" : {
        "<a href="#configid" title="ConfigId">ConfigId</a>" : <i>String</i>,
        "<a href="#instancecount" title="InstanceCount">InstanceCount</a>" : <i>Double</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::ReservedInstance
Properties:
    <a href="#configid" title="ConfigId">ConfigId</a>: <i>String</i>
    <a href="#instancecount" title="InstanceCount">InstanceCount</a>: <i>Double</i>
</pre>

## Properties

#### ConfigId

Configuration id of the reserved instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceCount

Number of reserved instances to be purchased.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### EndTime

Returns the <code>EndTime</code> value.

#### StartTime

Returns the <code>StartTime</code> value.

#### Status

Returns the <code>Status</code> value.

