# TF::Cloudflare::WafPackage

Provides a Cloudflare WAF rule package resource for a particular zone. This can be used to configure firewall behaviour for pre-defined firewall packages.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Cloudflare::WafPackage",
    "Properties" : {
        "<a href="#actionmode" title="ActionMode">ActionMode</a>" : <i>String</i>,
        "<a href="#packageid" title="PackageId">PackageId</a>" : <i>String</i>,
        "<a href="#sensitivity" title="Sensitivity">Sensitivity</a>" : <i>String</i>,
        "<a href="#zoneid" title="ZoneId">ZoneId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Cloudflare::WafPackage
Properties:
    <a href="#actionmode" title="ActionMode">ActionMode</a>: <i>String</i>
    <a href="#packageid" title="PackageId">PackageId</a>: <i>String</i>
    <a href="#sensitivity" title="Sensitivity">Sensitivity</a>: <i>String</i>
    <a href="#zoneid" title="ZoneId">ZoneId</a>: <i>String</i>
</pre>

## Properties

#### ActionMode

The action mode of the package, can be one of ["block", "challenge", "simulate"].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PackageId

The WAF Package ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sensitivity

The sensitivity of the package, can be one of ["high", "medium", "low", "off"].

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

#### Id

Returns the <code>Id</code> value.

