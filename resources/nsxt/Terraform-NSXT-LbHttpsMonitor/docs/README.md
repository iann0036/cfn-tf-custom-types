# Terraform::NSXT::LbHttpsMonitor

Provides a resource to configure lb https monitor on NSX-T manager

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::NSXT::LbHttpsMonitor",
    "Properties" : {
        "<a href="#certificatechaindepth" title="CertificateChainDepth">CertificateChainDepth</a>" : <i>Double</i>,
        "<a href="#ciphers" title="Ciphers">Ciphers</a>" : <i>[ String, ... ]</i>,
        "<a href="#clientcertificateid" title="ClientCertificateId">ClientCertificateId</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#fallcount" title="FallCount">FallCount</a>" : <i>Double</i>,
        "<a href="#interval" title="Interval">Interval</a>" : <i>Double</i>,
        "<a href="#monitorport" title="MonitorPort">MonitorPort</a>" : <i>String</i>,
        "<a href="#protocols" title="Protocols">Protocols</a>" : <i>[ String, ... ]</i>,
        "<a href="#requestbody" title="RequestBody">RequestBody</a>" : <i>String</i>,
        "<a href="#requestmethod" title="RequestMethod">RequestMethod</a>" : <i>String</i>,
        "<a href="#requesturl" title="RequestUrl">RequestUrl</a>" : <i>String</i>,
        "<a href="#requestversion" title="RequestVersion">RequestVersion</a>" : <i>String</i>,
        "<a href="#responsebody" title="ResponseBody">ResponseBody</a>" : <i>String</i>,
        "<a href="#responsestatuscodes" title="ResponseStatusCodes">ResponseStatusCodes</a>" : <i>[ Double, ... ]</i>,
        "<a href="#risecount" title="RiseCount">RiseCount</a>" : <i>Double</i>,
        "<a href="#serverauth" title="ServerAuth">ServerAuth</a>" : <i>String</i>,
        "<a href="#serverauthcaids" title="ServerAuthCaIds">ServerAuthCaIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#serverauthcrlids" title="ServerAuthCrlIds">ServerAuthCrlIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
        "<a href="#requestheader" title="RequestHeader">RequestHeader</a>" : <i>[ <a href="requestheader.md">RequestHeader</a>, ... ]</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tag.md">Tag</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::NSXT::LbHttpsMonitor
Properties:
    <a href="#certificatechaindepth" title="CertificateChainDepth">CertificateChainDepth</a>: <i>Double</i>
    <a href="#ciphers" title="Ciphers">Ciphers</a>: <i>
      - String</i>
    <a href="#clientcertificateid" title="ClientCertificateId">ClientCertificateId</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#fallcount" title="FallCount">FallCount</a>: <i>Double</i>
    <a href="#interval" title="Interval">Interval</a>: <i>Double</i>
    <a href="#monitorport" title="MonitorPort">MonitorPort</a>: <i>String</i>
    <a href="#protocols" title="Protocols">Protocols</a>: <i>
      - String</i>
    <a href="#requestbody" title="RequestBody">RequestBody</a>: <i>String</i>
    <a href="#requestmethod" title="RequestMethod">RequestMethod</a>: <i>String</i>
    <a href="#requesturl" title="RequestUrl">RequestUrl</a>: <i>String</i>
    <a href="#requestversion" title="RequestVersion">RequestVersion</a>: <i>String</i>
    <a href="#responsebody" title="ResponseBody">ResponseBody</a>: <i>String</i>
    <a href="#responsestatuscodes" title="ResponseStatusCodes">ResponseStatusCodes</a>: <i>
      - Double</i>
    <a href="#risecount" title="RiseCount">RiseCount</a>: <i>Double</i>
    <a href="#serverauth" title="ServerAuth">ServerAuth</a>: <i>String</i>
    <a href="#serverauthcaids" title="ServerAuthCaIds">ServerAuthCaIds</a>: <i>
      - String</i>
    <a href="#serverauthcrlids" title="ServerAuthCrlIds">ServerAuthCrlIds</a>: <i>
      - String</i>
    <a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
    <a href="#requestheader" title="RequestHeader">RequestHeader</a>: <i>
      - <a href="requestheader.md">RequestHeader</a></i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tag.md">Tag</a></i>
</pre>

## Properties

#### CertificateChainDepth

Authentication depth is used to set the verification depth in the server certificates chain.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ciphers

List of supported SSL ciphers.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientCertificateId

Client certificate can be specified to support client authentication.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

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

#### FallCount

Number of consecutive checks that must fail before marking it down.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interval

The frequency at which the system issues the monitor check (in seconds).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitorPort

If the monitor port is specified, it would override pool member port setting for healthcheck. A port range is not supported.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocols

SSL versions TLS1.1 and TLS1.2 are supported and enabled by default. SSLv2, SSLv3, and TLS1.0 are supported, but disabled by default.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestBody

String to send as HTTP health check request body. Valid only for certain HTTP methods like POST.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestMethod

Health check method for HTTP monitor type. Valid values are GET, HEAD, PUT, POST and OPTIONS.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestUrl

URL used for HTTP monitor.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestVersion

HTTP request version. Valid values are HTTP_VERSION_1_0 and HTTP_VERSION_1_1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseBody

If response body is specified, healthcheck HTTP response body is matched against the specified string and server is considered healthy only if there is a match (regular expressions not supported). If response body string is not specified, HTTP healthcheck is considered successful if the HTTP response status code is among configured values.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseStatusCodes

HTTP response status code should be a valid HTTP status code.

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RiseCount

Number of consecutive checks that must pass before marking it up.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerAuth

Server authentication mode - REQUIRED or IGNORE.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerAuthCaIds

If server auth type is REQUIRED, server certificate must be signed by one of the trusted Certificate Authorities (CAs), also referred to as root CAs, whose self signed certificates are specified.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerAuthCrlIds

A Certificate Revocation List (CRL) can be specified in the server-side SSL profile binding to disallow compromised server certificates.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

Number of seconds the target has to respond to the monitor request.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestHeader

_Required_: No

_Type_: List of <a href="requestheader.md">RequestHeader</a>

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

#### IsSecure

Returns the <code>IsSecure</code> value.

#### Revision

Returns the <code>Revision</code> value.

