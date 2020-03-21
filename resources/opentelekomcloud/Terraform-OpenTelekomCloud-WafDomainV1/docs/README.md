# Terraform::OpenTelekomCloud::WafDomainV1

Manages a WAF domain resource within OpenTelekomCloud.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenTelekomCloud::WafDomainV1",
    "Properties" : {
        "<a href="#certificateid" title="CertificateId">CertificateId</a>" : <i>String</i>,
        "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
        "<a href="#policyid" title="PolicyId">PolicyId</a>" : <i>String</i>,
        "<a href="#proxy" title="Proxy">Proxy</a>" : <i>Boolean</i>,
        "<a href="#sipheaderlist" title="SipHeaderList">SipHeaderList</a>" : <i>[ String, ... ]</i>,
        "<a href="#sipheadername" title="SipHeaderName">SipHeaderName</a>" : <i>String</i>,
        "<a href="#server" title="Server">Server</a>" : <i>[ <a href="server.md">Server</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenTelekomCloud::WafDomainV1
Properties:
    <a href="#certificateid" title="CertificateId">CertificateId</a>: <i>String</i>
    <a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
    <a href="#policyid" title="PolicyId">PolicyId</a>: <i>String</i>
    <a href="#proxy" title="Proxy">Proxy</a>: <i>Boolean</i>
    <a href="#sipheaderlist" title="SipHeaderList">SipHeaderList</a>: <i>
      - String</i>
    <a href="#sipheadername" title="SipHeaderName">SipHeaderName</a>: <i>String</i>
    <a href="#server" title="Server">Server</a>: <i>
      - <a href="server.md">Server</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### CertificateId

The certificate ID. This parameter is mandatory when front_protocol is set to HTTPS.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

The domain name. For example, www.example.com or *.example.com. Changing this creates a new domain.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyId

The policy ID associate with the domain. Changing this create a new domain.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Proxy

Specifies whether a proxy is configured.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SipHeaderList

Array of HTTP request header for identifying the real source IP address. This parameter is required only when proxy is set to true.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SipHeaderName

The type of the source IP header. This parameter is required only when proxy is set to true. The options are as follows: default, cloudflare, akamai, and custom.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Server

_Required_: No

_Type_: List of <a href="server.md">Server</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AccessCode

Returns the <code>AccessCode</code> value.

#### AccessStatus

Returns the <code>AccessStatus</code> value.

#### Cname

Returns the <code>Cname</code> value.

#### ProtectStatus

Returns the <code>ProtectStatus</code> value.

#### Protocol

Returns the <code>Protocol</code> value.

#### SubDomain

Returns the <code>SubDomain</code> value.

#### TxtCode

Returns the <code>TxtCode</code> value.

