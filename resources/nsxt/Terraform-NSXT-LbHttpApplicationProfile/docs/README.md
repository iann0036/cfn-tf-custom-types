# Terraform::NSXT::LbHttpApplicationProfile

Provides a resource to configure LB HTTP application profile on NSX-T manager

~> **NOTE:** This resource requires NSX version 2.3 or higher.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::NSXT::LbHttpApplicationProfile",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#httpredirectto" title="HttpRedirectTo">HttpRedirectTo</a>" : <i>String</i>,
        "<a href="#httpredirecttohttps" title="HttpRedirectToHttps">HttpRedirectToHttps</a>" : <i>Boolean</i>,
        "<a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>" : <i>Double</i>,
        "<a href="#ntlm" title="Ntlm">Ntlm</a>" : <i>Boolean</i>,
        "<a href="#requestbodysize" title="RequestBodySize">RequestBodySize</a>" : <i>Double</i>,
        "<a href="#requestheadersize" title="RequestHeaderSize">RequestHeaderSize</a>" : <i>Double</i>,
        "<a href="#responsetimeout" title="ResponseTimeout">ResponseTimeout</a>" : <i>Double</i>,
        "<a href="#xforwardedfor" title="XForwardedFor">XForwardedFor</a>" : <i>String</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tag.md">Tag</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::NSXT::LbHttpApplicationProfile
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#httpredirectto" title="HttpRedirectTo">HttpRedirectTo</a>: <i>String</i>
    <a href="#httpredirecttohttps" title="HttpRedirectToHttps">HttpRedirectToHttps</a>: <i>Boolean</i>
    <a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>: <i>Double</i>
    <a href="#ntlm" title="Ntlm">Ntlm</a>: <i>Boolean</i>
    <a href="#requestbodysize" title="RequestBodySize">RequestBodySize</a>: <i>Double</i>
    <a href="#requestheadersize" title="RequestHeaderSize">RequestHeaderSize</a>: <i>Double</i>
    <a href="#responsetimeout" title="ResponseTimeout">ResponseTimeout</a>: <i>Double</i>
    <a href="#xforwardedfor" title="XForwardedFor">XForwardedFor</a>: <i>String</i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tag.md">Tag</a></i>
</pre>

## Properties

#### Description

Description of this resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

The display name of this resource. Defaults to ID if not set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpRedirectTo

A URL that incoming requests for that virtual server can be temporarily redirected to, If a website is temporarily down or has moved. When set, http_redirect_to_https should be false.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpRedirectToHttps

A boolean flag which reflects whether the client will automatically be redirected to use SSL. When true, the http_redirect_to should not be specified.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdleTimeout

Timeout in seconds to specify how long an HTTP application can remain idle. Defaults to 15 seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ntlm

A boolean flag which reflects whether NTLM challenge/response methodology will be used over HTTP. Can be set to true only if http_redirect_to_https is false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestBodySize

Maximum request body size in bytes. If it is not specified, it means that request body size is unlimited.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestHeaderSize

Maximum request header size in bytes. Requests with larger header size will be processed as best effort whereas a request with header below this specified size is guaranteed to be processed. Defaults to 1024 bytes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseTimeout

Number of seconds waiting for the server response before the connection is closed. Defaults to 60 seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### XForwardedFor

When this value is set, the x_forwarded_for header in the incoming request will be inserted or replaced. Supported values are "INSERT" and "REPLACE".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tag.md">Tag</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Revision

Returns the <code>Revision</code> value.

