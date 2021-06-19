# TF::TencentCloud::ApiGatewayCustomDomain

Use this resource to create custom domain of API gateway.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::ApiGatewayCustomDomain",
    "Properties" : {
        "<a href="#certificateid" title="CertificateId">CertificateId</a>" : <i>String</i>,
        "<a href="#defaultdomain" title="DefaultDomain">DefaultDomain</a>" : <i>String</i>,
        "<a href="#isdefaultmapping" title="IsDefaultMapping">IsDefaultMapping</a>" : <i>Boolean</i>,
        "<a href="#nettype" title="NetType">NetType</a>" : <i>String</i>,
        "<a href="#pathmappings" title="PathMappings">PathMappings</a>" : <i>[ String, ... ]</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#serviceid" title="ServiceId">ServiceId</a>" : <i>String</i>,
        "<a href="#subdomain" title="SubDomain">SubDomain</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::ApiGatewayCustomDomain
Properties:
    <a href="#certificateid" title="CertificateId">CertificateId</a>: <i>String</i>
    <a href="#defaultdomain" title="DefaultDomain">DefaultDomain</a>: <i>String</i>
    <a href="#isdefaultmapping" title="IsDefaultMapping">IsDefaultMapping</a>: <i>Boolean</i>
    <a href="#nettype" title="NetType">NetType</a>: <i>String</i>
    <a href="#pathmappings" title="PathMappings">PathMappings</a>: <i>
      - String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#serviceid" title="ServiceId">ServiceId</a>: <i>String</i>
    <a href="#subdomain" title="SubDomain">SubDomain</a>: <i>String</i>
</pre>

## Properties

#### CertificateId

Unique certificate ID of the custom domain name to be bound. You can choose to upload for the `protocol` attribute value `https` or `http&https`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultDomain

Default domain name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsDefaultMapping

Whether the default path mapping is used. The default value is `true`. When it is `false`, it means custom path mapping. In this case, the `path_mappings` attribute is required.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetType

Network type. Valid values: `OUTER`, `INNER`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathMappings

Custom domain name path mapping. The data format is: `path#environment`. Optional values for the environment are `test`, `prepub`, and `release`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Protocol supported by service. Valid values: `http`, `https`, `http&https`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceId

Unique service ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubDomain

Custom domain name to be bound.

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

#### Status

Returns the <code>Status</code> value.

