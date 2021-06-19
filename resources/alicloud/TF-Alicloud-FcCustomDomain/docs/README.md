# TF::Alicloud::FcCustomDomain

CloudFormation equivalent of alicloud_fc_custom_domain

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::FcCustomDomain",
    "Properties" : {
        "<a href="#domainname" title="DomainName">DomainName</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#certconfig" title="CertConfig">CertConfig</a>" : <i>[ <a href="certconfigdefinition.md">CertConfigDefinition</a>, ... ]</i>,
        "<a href="#routeconfig" title="RouteConfig">RouteConfig</a>" : <i>[ <a href="routeconfigdefinition.md">RouteConfigDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::FcCustomDomain
Properties:
    <a href="#domainname" title="DomainName">DomainName</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#certconfig" title="CertConfig">CertConfig</a>: <i>
      - <a href="certconfigdefinition.md">CertConfigDefinition</a></i>
    <a href="#routeconfig" title="RouteConfig">RouteConfig</a>: <i>
      - <a href="routeconfigdefinition.md">RouteConfigDefinition</a></i>
</pre>

## Properties

#### DomainName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertConfig

_Required_: No

_Type_: List of <a href="certconfigdefinition.md">CertConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteConfig

_Required_: No

_Type_: List of <a href="routeconfigdefinition.md">RouteConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AccountId

Returns the <code>AccountId</code> value.

#### ApiVersion

Returns the <code>ApiVersion</code> value.

#### CreatedTime

Returns the <code>CreatedTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### LastModifiedTime

Returns the <code>LastModifiedTime</code> value.

