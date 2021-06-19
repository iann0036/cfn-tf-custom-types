# TF::Alicloud::DdoscooDomainResource

CloudFormation equivalent of alicloud_ddoscoo_domain_resource

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::DdoscooDomainResource",
    "Properties" : {
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#httpsext" title="HttpsExt">HttpsExt</a>" : <i>String</i>,
        "<a href="#instanceids" title="InstanceIds">InstanceIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#realservers" title="RealServers">RealServers</a>" : <i>[ String, ... ]</i>,
        "<a href="#rstype" title="RsType">RsType</a>" : <i>Double</i>,
        "<a href="#proxytypes" title="ProxyTypes">ProxyTypes</a>" : <i>[ <a href="proxytypesdefinition.md">ProxyTypesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::DdoscooDomainResource
Properties:
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#httpsext" title="HttpsExt">HttpsExt</a>: <i>String</i>
    <a href="#instanceids" title="InstanceIds">InstanceIds</a>: <i>
      - String</i>
    <a href="#realservers" title="RealServers">RealServers</a>: <i>
      - String</i>
    <a href="#rstype" title="RsType">RsType</a>: <i>Double</i>
    <a href="#proxytypes" title="ProxyTypes">ProxyTypes</a>: <i>
      - <a href="proxytypesdefinition.md">ProxyTypesDefinition</a></i>
</pre>

## Properties

#### Domain

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpsExt

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceIds

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RealServers

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RsType

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyTypes

_Required_: No

_Type_: List of <a href="proxytypesdefinition.md">ProxyTypesDefinition</a>

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

