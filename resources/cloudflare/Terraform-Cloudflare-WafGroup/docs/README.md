# Terraform::Cloudflare::WafGroup

Provides a Cloudflare WAF rule group resource for a particular zone. This can be used to configure firewall behaviour for pre-defined firewall groups.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Cloudflare::WafGroup",
    "Properties" : {
        "<a href="#groupid" title="GroupId">GroupId</a>" : <i>String</i>,
        "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
        "<a href="#packageid" title="PackageId">PackageId</a>" : <i>String</i>,
        "<a href="#zoneid" title="ZoneId">ZoneId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Cloudflare::WafGroup
Properties:
    <a href="#groupid" title="GroupId">GroupId</a>: <i>String</i>
    <a href="#mode" title="Mode">Mode</a>: <i>String</i>
    <a href="#packageid" title="PackageId">PackageId</a>: <i>String</i>
    <a href="#zoneid" title="ZoneId">ZoneId</a>: <i>String</i>
</pre>

## Properties

#### GroupId

The WAF Rule Group ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

The mode of the group, can be one of ["on", "off"].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PackageId

The ID of the WAF Rule Package that contains the group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneId

The DNS zone ID to apply to.

_Required_: Yes

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

