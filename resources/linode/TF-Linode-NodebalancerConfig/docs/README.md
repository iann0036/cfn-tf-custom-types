# TF::Linode::NodebalancerConfig

Provides a Linode NodeBalancer Config resource.  This can be used to create, modify, and delete Linodes NodeBalancer Configs.
For more information, see [Getting Started with NodeBalancers](https://www.linode.com/docs/platform/nodebalancer/getting-started-with-nodebalancers/) and the [Linode APIv4 docs](https://developers.linode.com/api/v4#operation/createNodeBalancerConfig).

The Linode Guide, [Create a NodeBalancer with Terraform](https://www.linode.com/docs/applications/configuration-management/create-a-nodebalancer-with-terraform/), provides step-by-step guidance and additional examples.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Linode::NodebalancerConfig",
    "Properties" : {
        "<a href="#algorithm" title="Algorithm">Algorithm</a>" : <i>String</i>,
        "<a href="#check" title="Check">Check</a>" : <i>String</i>,
        "<a href="#checkattempts" title="CheckAttempts">CheckAttempts</a>" : <i>Double</i>,
        "<a href="#checkbody" title="CheckBody">CheckBody</a>" : <i>String</i>,
        "<a href="#checkinterval" title="CheckInterval">CheckInterval</a>" : <i>Double</i>,
        "<a href="#checkpassive" title="CheckPassive">CheckPassive</a>" : <i>Boolean</i>,
        "<a href="#checkpath" title="CheckPath">CheckPath</a>" : <i>String</i>,
        "<a href="#checktimeout" title="CheckTimeout">CheckTimeout</a>" : <i>Double</i>,
        "<a href="#ciphersuite" title="CipherSuite">CipherSuite</a>" : <i>String</i>,
        "<a href="#nodebalancerid" title="NodebalancerId">NodebalancerId</a>" : <i>Double</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#proxyprotocol" title="ProxyProtocol">ProxyProtocol</a>" : <i>String</i>,
        "<a href="#sslcert" title="SslCert">SslCert</a>" : <i>String</i>,
        "<a href="#sslkey" title="SslKey">SslKey</a>" : <i>String</i>,
        "<a href="#stickiness" title="Stickiness">Stickiness</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Linode::NodebalancerConfig
Properties:
    <a href="#algorithm" title="Algorithm">Algorithm</a>: <i>String</i>
    <a href="#check" title="Check">Check</a>: <i>String</i>
    <a href="#checkattempts" title="CheckAttempts">CheckAttempts</a>: <i>Double</i>
    <a href="#checkbody" title="CheckBody">CheckBody</a>: <i>String</i>
    <a href="#checkinterval" title="CheckInterval">CheckInterval</a>: <i>Double</i>
    <a href="#checkpassive" title="CheckPassive">CheckPassive</a>: <i>Boolean</i>
    <a href="#checkpath" title="CheckPath">CheckPath</a>: <i>String</i>
    <a href="#checktimeout" title="CheckTimeout">CheckTimeout</a>: <i>Double</i>
    <a href="#ciphersuite" title="CipherSuite">CipherSuite</a>: <i>String</i>
    <a href="#nodebalancerid" title="NodebalancerId">NodebalancerId</a>: <i>Double</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#proxyprotocol" title="ProxyProtocol">ProxyProtocol</a>: <i>String</i>
    <a href="#sslcert" title="SslCert">SslCert</a>: <i>String</i>
    <a href="#sslkey" title="SslKey">SslKey</a>: <i>String</i>
    <a href="#stickiness" title="Stickiness">Stickiness</a>: <i>String</i>
</pre>

## Properties

#### Algorithm

What algorithm this NodeBalancer should use for routing traffic to backends. (`roundrobin`, `leastconn`, `source`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Check

The type of check to perform against backends to ensure they are serving requests. This is used to determine if backends are up or down. If none no check is performed. connection requires only a connection to the backend to succeed. http and http_body rely on the backend serving HTTP, and that the response returned matches what is expected. (`none`, `connection`, `http`, `http_body`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckAttempts

How many times to attempt a check before considering a backend to be down. (1-30).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckBody

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckInterval

How often, in seconds, to check that backends are up and serving requests.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckPassive

If true, any response from this backend with a 5xx status code will be enough for it to be considered unhealthy and taken out of rotation.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckPath

The URL path to check on each backend. If the backend does not respond to this request it is considered to be down.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckTimeout

How long, in seconds, to wait for a check attempt before considering it failed. (1-30).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CipherSuite

What ciphers to use for SSL connections served by this NodeBalancer. `legacy` is considered insecure and should only be used if necessary.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodebalancerId

The ID of the NodeBalancer to access.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

The TCP port this Config is for. These values must be unique across configs on a single NodeBalancer (you can't have two configs for port 80, for example). While some ports imply some protocols, no enforcement is done and you may configure your NodeBalancer however is useful to you. For example, while port 443 is generally used for HTTPS, you do not need SSL configured to have a NodeBalancer listening on port 443. (Defaults to 80).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

The protocol this port is configured to serve. If this is set to https you must include an ssl_cert and an ssl_key. (`http`, `https`, `tcp`) (Defaults to `http`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyProtocol

The version of ProxyProtocol to use for the underlying NodeBalancer. This requires protocol to be `tcp`. (`none`, `v1`, `v2`) (Defaults to `none`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCert

The certificate this port is serving. This is not returned. If set, this field will come back as `<REDACTED>`. Please use the ssl_commonname and ssl_fingerprint to identify the certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslKey

The private key corresponding to this port's certificate. This is not returned. If set, this field will come back as `<REDACTED>`. Please use the ssl_commonname and ssl_fingerprint to identify the certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Stickiness

Controls how session stickiness is handled on this port. (`none`, `table`, `http_cookie`).

_Required_: No

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

#### NodeStatus

Returns the <code>NodeStatus</code> value.

#### SslCommonname

Returns the <code>SslCommonname</code> value.

#### SslFingerprint

Returns the <code>SslFingerprint</code> value.

