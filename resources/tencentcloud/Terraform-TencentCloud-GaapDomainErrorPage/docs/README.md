# Terraform::TencentCloud::GaapDomainErrorPage

Provide a resource to custom error page info for a GAAP HTTP domain.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::GaapDomainErrorPage",
    "Properties" : {
        "<a href="#body" title="Body">Body</a>" : <i>String</i>,
        "<a href="#clearheaders" title="ClearHeaders">ClearHeaders</a>" : <i>[ String, ... ]</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#errorcodes" title="ErrorCodes">ErrorCodes</a>" : <i>[ Double, ... ]</i>,
        "<a href="#listenerid" title="ListenerId">ListenerId</a>" : <i>String</i>,
        "<a href="#newerrorcode" title="NewErrorCode">NewErrorCode</a>" : <i>Double</i>,
        "<a href="#setheaders" title="SetHeaders">SetHeaders</a>" : <i>[ <a href="setheaders.md">SetHeaders</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::GaapDomainErrorPage
Properties:
    <a href="#body" title="Body">Body</a>: <i>String</i>
    <a href="#clearheaders" title="ClearHeaders">ClearHeaders</a>: <i>
      - String</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#errorcodes" title="ErrorCodes">ErrorCodes</a>: <i>
      - Double</i>
    <a href="#listenerid" title="ListenerId">ListenerId</a>: <i>String</i>
    <a href="#newerrorcode" title="NewErrorCode">NewErrorCode</a>: <i>Double</i>
    <a href="#setheaders" title="SetHeaders">SetHeaders</a>: <i>
      - <a href="setheaders.md">SetHeaders</a></i>
</pre>

## Properties

#### Body

New response body.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClearHeaders

Response headers to be removed.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

HTTP domain.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ErrorCodes

Original error codes.

_Required_: Yes

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ListenerId

ID of the layer7 listener.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NewErrorCode

New error code.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetHeaders

Response headers to be set.

_Required_: No

_Type_: List of <a href="setheaders.md">SetHeaders</a>

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

