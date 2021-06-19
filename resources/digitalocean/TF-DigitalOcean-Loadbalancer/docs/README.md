# TF::DigitalOcean::Loadbalancer

Provides a DigitalOcean Load Balancer resource. This can be used to create,
modify, and delete Load Balancers.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::DigitalOcean::Loadbalancer",
    "Properties" : {
        "<a href="#algorithm" title="Algorithm">Algorithm</a>" : <i>String</i>,
        "<a href="#dropletids" title="DropletIds">DropletIds</a>" : <i>[ Double, ... ]</i>,
        "<a href="#droplettag" title="DropletTag">DropletTag</a>" : <i>String</i>,
        "<a href="#enablebackendkeepalive" title="EnableBackendKeepalive">EnableBackendKeepalive</a>" : <i>Boolean</i>,
        "<a href="#enableproxyprotocol" title="EnableProxyProtocol">EnableProxyProtocol</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#redirecthttptohttps" title="RedirectHttpToHttps">RedirectHttpToHttps</a>" : <i>Boolean</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#size" title="Size">Size</a>" : <i>String</i>,
        "<a href="#vpcuuid" title="VpcUuid">VpcUuid</a>" : <i>String</i>,
        "<a href="#forwardingrule" title="ForwardingRule">ForwardingRule</a>" : <i>[ <a href="forwardingruledefinition.md">ForwardingRuleDefinition</a>, ... ]</i>,
        "<a href="#healthcheck" title="Healthcheck">Healthcheck</a>" : <i>[ <a href="healthcheckdefinition.md">HealthcheckDefinition</a>, ... ]</i>,
        "<a href="#stickysessions" title="StickySessions">StickySessions</a>" : <i>[ <a href="stickysessionsdefinition.md">StickySessionsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::DigitalOcean::Loadbalancer
Properties:
    <a href="#algorithm" title="Algorithm">Algorithm</a>: <i>String</i>
    <a href="#dropletids" title="DropletIds">DropletIds</a>: <i>
      - Double</i>
    <a href="#droplettag" title="DropletTag">DropletTag</a>: <i>String</i>
    <a href="#enablebackendkeepalive" title="EnableBackendKeepalive">EnableBackendKeepalive</a>: <i>Boolean</i>
    <a href="#enableproxyprotocol" title="EnableProxyProtocol">EnableProxyProtocol</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#redirecthttptohttps" title="RedirectHttpToHttps">RedirectHttpToHttps</a>: <i>Boolean</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#size" title="Size">Size</a>: <i>String</i>
    <a href="#vpcuuid" title="VpcUuid">VpcUuid</a>: <i>String</i>
    <a href="#forwardingrule" title="ForwardingRule">ForwardingRule</a>: <i>
      - <a href="forwardingruledefinition.md">ForwardingRuleDefinition</a></i>
    <a href="#healthcheck" title="Healthcheck">Healthcheck</a>: <i>
      - <a href="healthcheckdefinition.md">HealthcheckDefinition</a></i>
    <a href="#stickysessions" title="StickySessions">StickySessions</a>: <i>
      - <a href="stickysessionsdefinition.md">StickySessionsDefinition</a></i>
</pre>

## Properties

#### Algorithm

The load balancing algorithm used to determine
which backend Droplet will be selected by a client. It must be either `round_robin`
or `least_connections`. The default value is `round_robin`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DropletIds

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DropletTag

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableBackendKeepalive

A boolean value indicating whether HTTP keepalive connections are maintained to target Droplets. Default value is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableProxyProtocol

A boolean value indicating whether PROXY
Protocol should be used to pass information from connecting client requests to
the backend service. Default value is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The Load Balancer name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectHttpToHttps

A boolean value indicating whether
HTTP requests to the Load Balancer on port 80 will be redirected to HTTPS on port 443.
Default value is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region to start in.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

The size of the Load Balancer. It must be either `lb-small`, `lb-medium`, or `lb-large`. Defaults to `lb-small`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcUuid

The ID of the VPC where the load balancer will be located.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardingRule

_Required_: No

_Type_: List of <a href="forwardingruledefinition.md">ForwardingRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Healthcheck

_Required_: No

_Type_: List of <a href="healthcheckdefinition.md">HealthcheckDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StickySessions

_Required_: No

_Type_: List of <a href="stickysessionsdefinition.md">StickySessionsDefinition</a>

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

#### Ip

Returns the <code>Ip</code> value.

#### Status

Returns the <code>Status</code> value.

#### Urn

Returns the <code>Urn</code> value.

