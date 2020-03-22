# Terraform::BIGIP::LtmProfileHttp

`bigip_ltm_profile_http` Configures a custom profile_http for use by health checks.

For resources should be named with their "full path". The full path is the combination of the partition + name of the resource. For example /Common/my-pool.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::BIGIP::LtmProfileHttp",
    "Properties" : {
        "<a href="#acceptxff" title="AcceptXff">AcceptXff</a>" : <i>String</i>,
        "<a href="#appservice" title="AppService">AppService</a>" : <i>String</i>,
        "<a href="#basicauthrealm" title="BasicAuthRealm">BasicAuthRealm</a>" : <i>String</i>,
        "<a href="#defaultsfrom" title="DefaultsFrom">DefaultsFrom</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#encryptcookiesecret" title="EncryptCookieSecret">EncryptCookieSecret</a>" : <i>String</i>,
        "<a href="#encryptcookies" title="EncryptCookies">EncryptCookies</a>" : <i>[ String, ... ]</i>,
        "<a href="#fallbackhost" title="FallbackHost">FallbackHost</a>" : <i>String</i>,
        "<a href="#fallbackstatuscodes" title="FallbackStatusCodes">FallbackStatusCodes</a>" : <i>[ String, ... ]</i>,
        "<a href="#headerase" title="HeadErase">HeadErase</a>" : <i>String</i>,
        "<a href="#headinsert" title="HeadInsert">HeadInsert</a>" : <i>String</i>,
        "<a href="#insertxforwardedfor" title="InsertXforwardedFor">InsertXforwardedFor</a>" : <i>String</i>,
        "<a href="#lwsseparator" title="LwsSeparator">LwsSeparator</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#oneconnecttransformations" title="OneconnectTransformations">OneconnectTransformations</a>" : <i>String</i>,
        "<a href="#proxytype" title="ProxyType">ProxyType</a>" : <i>String</i>,
        "<a href="#redirectrewrite" title="RedirectRewrite">RedirectRewrite</a>" : <i>String</i>,
        "<a href="#requestchunking" title="RequestChunking">RequestChunking</a>" : <i>String</i>,
        "<a href="#responsechunking" title="ResponseChunking">ResponseChunking</a>" : <i>String</i>,
        "<a href="#responseheaderspermitted" title="ResponseHeadersPermitted">ResponseHeadersPermitted</a>" : <i>[ String, ... ]</i>,
        "<a href="#serveragentname" title="ServerAgentName">ServerAgentName</a>" : <i>String</i>,
        "<a href="#tmpartition" title="TmPartition">TmPartition</a>" : <i>String</i>,
        "<a href="#viahostname" title="ViaHostName">ViaHostName</a>" : <i>String</i>,
        "<a href="#viarequest" title="ViaRequest">ViaRequest</a>" : <i>String</i>,
        "<a href="#viaresponse" title="ViaResponse">ViaResponse</a>" : <i>String</i>,
        "<a href="#xffalternativenames" title="XffAlternativeNames">XffAlternativeNames</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::BIGIP::LtmProfileHttp
Properties:
    <a href="#acceptxff" title="AcceptXff">AcceptXff</a>: <i>String</i>
    <a href="#appservice" title="AppService">AppService</a>: <i>String</i>
    <a href="#basicauthrealm" title="BasicAuthRealm">BasicAuthRealm</a>: <i>String</i>
    <a href="#defaultsfrom" title="DefaultsFrom">DefaultsFrom</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#encryptcookiesecret" title="EncryptCookieSecret">EncryptCookieSecret</a>: <i>String</i>
    <a href="#encryptcookies" title="EncryptCookies">EncryptCookies</a>: <i>
      - String</i>
    <a href="#fallbackhost" title="FallbackHost">FallbackHost</a>: <i>String</i>
    <a href="#fallbackstatuscodes" title="FallbackStatusCodes">FallbackStatusCodes</a>: <i>
      - String</i>
    <a href="#headerase" title="HeadErase">HeadErase</a>: <i>String</i>
    <a href="#headinsert" title="HeadInsert">HeadInsert</a>: <i>String</i>
    <a href="#insertxforwardedfor" title="InsertXforwardedFor">InsertXforwardedFor</a>: <i>String</i>
    <a href="#lwsseparator" title="LwsSeparator">LwsSeparator</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#oneconnecttransformations" title="OneconnectTransformations">OneconnectTransformations</a>: <i>String</i>
    <a href="#proxytype" title="ProxyType">ProxyType</a>: <i>String</i>
    <a href="#redirectrewrite" title="RedirectRewrite">RedirectRewrite</a>: <i>String</i>
    <a href="#requestchunking" title="RequestChunking">RequestChunking</a>: <i>String</i>
    <a href="#responsechunking" title="ResponseChunking">ResponseChunking</a>: <i>String</i>
    <a href="#responseheaderspermitted" title="ResponseHeadersPermitted">ResponseHeadersPermitted</a>: <i>
      - String</i>
    <a href="#serveragentname" title="ServerAgentName">ServerAgentName</a>: <i>String</i>
    <a href="#tmpartition" title="TmPartition">TmPartition</a>: <i>String</i>
    <a href="#viahostname" title="ViaHostName">ViaHostName</a>: <i>String</i>
    <a href="#viarequest" title="ViaRequest">ViaRequest</a>: <i>String</i>
    <a href="#viaresponse" title="ViaResponse">ViaResponse</a>: <i>String</i>
    <a href="#xffalternativenames" title="XffAlternativeNames">XffAlternativeNames</a>: <i>
      - String</i>
</pre>

## Properties

#### AcceptXff

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppService

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BasicAuthRealm

Specifies a quoted string for the basic authentication realm. The system sends this string to a client whenever authorization fails. The default value is none.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultsFrom

Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptCookieSecret

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptCookies

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FallbackHost

Specifies an HTTP fallback host. HTTP redirection allows you to redirect HTTP traffic to another protocol identifier, host name, port number.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FallbackStatusCodes

Specifies one or more three-digit status codes that can be returned by an HTTP server.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeadErase

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeadInsert

Specifies a quoted header string that you want to insert into an HTTP request.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsertXforwardedFor

When using connection pooling, which allows clients to make use of other client requests' server-side connections, you can insert the X-Forwarded-For header and specify a client IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LwsSeparator

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OneconnectTransformations

Enables the system to perform HTTP header transformations for the purpose of  keeping server-side connections open. This feature requires configuration of a OneConnect profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectRewrite

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestChunking

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseChunking

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseHeadersPermitted

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerAgentName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TmPartition

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ViaHostName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ViaRequest

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ViaResponse

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### XffAlternativeNames

_Required_: No

_Type_: List of String

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

