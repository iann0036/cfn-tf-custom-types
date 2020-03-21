# Terraform::CloudStack::Firewall

Creates firewall rules for a given IP address.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::CloudStack::Firewall",
    "Properties" : {
        "<a href="#ipaddressid" title="IpAddressId">IpAddressId</a>" : <i>String</i>,
        "<a href="#managed" title="Managed">Managed</a>" : <i>Boolean</i>,
        "<a href="#parallelism" title="Parallelism">Parallelism</a>" : <i>Double</i>,
        "<a href="#rule" title="Rule">Rule</a>" : <i>[ <a href="rule.md">Rule</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::CloudStack::Firewall
Properties:
    <a href="#ipaddressid" title="IpAddressId">IpAddressId</a>: <i>String</i>
    <a href="#managed" title="Managed">Managed</a>: <i>Boolean</i>
    <a href="#parallelism" title="Parallelism">Parallelism</a>: <i>Double</i>
    <a href="#rule" title="Rule">Rule</a>: <i>
      - <a href="rule.md">Rule</a></i>
</pre>

## Properties

#### IpAddressId

The IP address ID for which to create the
firewall rules. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Managed

USE WITH CAUTION! If enabled all the firewall rules for
this IP address will be managed by this resource. This means it will delete
all firewall rules that are not in your config! (defaults false).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parallelism

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: No

_Type_: List of <a href="rule.md">Rule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

