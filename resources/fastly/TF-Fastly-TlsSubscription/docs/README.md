# TF::Fastly::TlsSubscription

Enables TLS on a domain using a certificate managed by Fastly.

DNS records need to be modified on the domain being secured, in order to respond to the ACME domain ownership challenge.

There are two options for doing this: the `managed_dns_challenge`, which is the default method; and the `managed_http_challenges`, which points production traffic to Fastly.

~> See the [Fastly documentation](https://docs.fastly.com/en/guides/serving-https-traffic-using-fastly-managed-certificates#verifying-domain-ownership) for more information on verifying domain ownership.

The example below demonstrates usage with AWS Route53 to configure DNS, and the `fastly_tls_subscription_validation` resource to wait for validation to complete.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Fastly::TlsSubscription",
    "Properties" : {
        "<a href="#certificateauthority" title="CertificateAuthority">CertificateAuthority</a>" : <i>String</i>,
        "<a href="#commonname" title="CommonName">CommonName</a>" : <i>String</i>,
        "<a href="#configurationid" title="ConfigurationId">ConfigurationId</a>" : <i>String</i>,
        "<a href="#domains" title="Domains">Domains</a>" : <i>[ String, ... ]</i>,
        "<a href="#forcedestroy" title="ForceDestroy">ForceDestroy</a>" : <i>Boolean</i>,
        "<a href="#forceupdate" title="ForceUpdate">ForceUpdate</a>" : <i>Boolean</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Fastly::TlsSubscription
Properties:
    <a href="#certificateauthority" title="CertificateAuthority">CertificateAuthority</a>: <i>String</i>
    <a href="#commonname" title="CommonName">CommonName</a>: <i>String</i>
    <a href="#configurationid" title="ConfigurationId">ConfigurationId</a>: <i>String</i>
    <a href="#domains" title="Domains">Domains</a>: <i>
      - String</i>
    <a href="#forcedestroy" title="ForceDestroy">ForceDestroy</a>: <i>Boolean</i>
    <a href="#forceupdate" title="ForceUpdate">ForceUpdate</a>: <i>Boolean</i>
</pre>

## Properties

#### CertificateAuthority

The entity that issues and certifies the TLS certificates for your subscription. Valid values are `lets-encrypt` or `globalsign`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CommonName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigurationId

The ID of the set of TLS configuration options that apply to the enabled domains on this subscription.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domains

List of domains on which to enable TLS.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceDestroy

Always delete subscription, even when active domains are present. Defaults to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceUpdate

Always update subscription, even when active domains are present. Defaults to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### Id

Returns the <code>Id</code> value.

#### ManagedDnsChallenge

Returns the <code>ManagedDnsChallenge</code> value.

#### ManagedHttpChallenges

Returns the <code>ManagedHttpChallenges</code> value.

#### State

Returns the <code>State</code> value.

#### UpdatedAt

Returns the <code>UpdatedAt</code> value.

