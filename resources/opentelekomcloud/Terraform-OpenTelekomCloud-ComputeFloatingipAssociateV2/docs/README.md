# Terraform::OpenTelekomCloud::ComputeFloatingipAssociateV2

Associate a floating IP to an instance. This can be used instead of the
`floating_ip` options in `opentelekomcloud_compute_instance_v2`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenTelekomCloud::ComputeFloatingipAssociateV2",
    "Properties" : {
        "<a href="#fixedip" title="FixedIp">FixedIp</a>" : <i>String</i>,
        "<a href="#floatingip" title="FloatingIp">FloatingIp</a>" : <i>String</i>,
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenTelekomCloud::ComputeFloatingipAssociateV2
Properties:
    <a href="#fixedip" title="FixedIp">FixedIp</a>: <i>String</i>
    <a href="#floatingip" title="FloatingIp">FloatingIp</a>: <i>String</i>
    <a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
</pre>

## Properties

#### FixedIp

The specific IP address to direct traffic to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FloatingIp

The floating IP to associate.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceId

The instance to associte the floating IP with.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

