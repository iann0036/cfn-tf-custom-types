# TF::Vultr::InstanceIpv4

CloudFormation equivalent of vultr_instance_ipv4

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Vultr::InstanceIpv4",
    "Properties" : {
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
        "<a href="#reboot" title="Reboot">Reboot</a>" : <i>Boolean</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Vultr::InstanceIpv4
Properties:
    <a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
    <a href="#reboot" title="Reboot">Reboot</a>: <i>Boolean</i>
</pre>

## Properties

#### InstanceId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Reboot

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Gateway

Returns the <code>Gateway</code> value.

#### Id

Returns the <code>Id</code> value.

#### Ip

Returns the <code>Ip</code> value.

#### Netmask

Returns the <code>Netmask</code> value.

#### Reverse

Returns the <code>Reverse</code> value.

