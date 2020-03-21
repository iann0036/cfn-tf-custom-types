# Terraform::AzureRM::Frontdoor

CloudFormation equivalent of azurerm_frontdoor

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::Frontdoor",
    "Properties" : {
        "<a href="#enforcebackendpoolscertificatenamecheck" title="EnforceBackendPoolsCertificateNameCheck">EnforceBackendPoolsCertificateNameCheck</a>" : <i>Boolean</i>,
        "<a href="#friendlyname" title="FriendlyName">FriendlyName</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#loadbalancerenabled" title="LoadBalancerEnabled">LoadBalancerEnabled</a>" : <i>Boolean</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#backendpool" title="BackendPool">BackendPool</a>" : <i>[ <a href="backendpool.md">BackendPool</a>, ... ]</i>,
        "<a href="#backendpoolhealthprobe" title="BackendPoolHealthProbe">BackendPoolHealthProbe</a>" : <i>[ <a href="backendpoolhealthprobe.md">BackendPoolHealthProbe</a>, ... ]</i>,
        "<a href="#backendpoolloadbalancing" title="BackendPoolLoadBalancing">BackendPoolLoadBalancing</a>" : <i>[ <a href="backendpoolloadbalancing.md">BackendPoolLoadBalancing</a>, ... ]</i>,
        "<a href="#frontendendpoint" title="FrontendEndpoint">FrontendEndpoint</a>" : <i>[ <a href="frontendendpoint.md">FrontendEndpoint</a>, ... ]</i>,
        "<a href="#routingrule" title="RoutingRule">RoutingRule</a>" : <i>[ <a href="routingrule.md">RoutingRule</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#backend" title="Backend">Backend</a>" : <i>[ <a href="backend.md">Backend</a>, ... ]</i>,
        "<a href="#customhttpsconfiguration" title="CustomHttpsConfiguration">CustomHttpsConfiguration</a>" : <i>[ <a href="customhttpsconfiguration.md">CustomHttpsConfiguration</a>, ... ]</i>,
        "<a href="#forwardingconfiguration" title="ForwardingConfiguration">ForwardingConfiguration</a>" : <i>[ <a href="forwardingconfiguration.md">ForwardingConfiguration</a>, ... ]</i>,
        "<a href="#redirectconfiguration" title="RedirectConfiguration">RedirectConfiguration</a>" : <i>[ <a href="redirectconfiguration.md">RedirectConfiguration</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::Frontdoor
Properties:
    <a href="#enforcebackendpoolscertificatenamecheck" title="EnforceBackendPoolsCertificateNameCheck">EnforceBackendPoolsCertificateNameCheck</a>: <i>Boolean</i>
    <a href="#friendlyname" title="FriendlyName">FriendlyName</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#loadbalancerenabled" title="LoadBalancerEnabled">LoadBalancerEnabled</a>: <i>Boolean</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#backendpool" title="BackendPool">BackendPool</a>: <i>
      - <a href="backendpool.md">BackendPool</a></i>
    <a href="#backendpoolhealthprobe" title="BackendPoolHealthProbe">BackendPoolHealthProbe</a>: <i>
      - <a href="backendpoolhealthprobe.md">BackendPoolHealthProbe</a></i>
    <a href="#backendpoolloadbalancing" title="BackendPoolLoadBalancing">BackendPoolLoadBalancing</a>: <i>
      - <a href="backendpoolloadbalancing.md">BackendPoolLoadBalancing</a></i>
    <a href="#frontendendpoint" title="FrontendEndpoint">FrontendEndpoint</a>: <i>
      - <a href="frontendendpoint.md">FrontendEndpoint</a></i>
    <a href="#routingrule" title="RoutingRule">RoutingRule</a>: <i>
      - <a href="routingrule.md">RoutingRule</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#backend" title="Backend">Backend</a>: <i>
      - <a href="backend.md">Backend</a></i>
    <a href="#customhttpsconfiguration" title="CustomHttpsConfiguration">CustomHttpsConfiguration</a>: <i>
      - <a href="customhttpsconfiguration.md">CustomHttpsConfiguration</a></i>
    <a href="#forwardingconfiguration" title="ForwardingConfiguration">ForwardingConfiguration</a>: <i>
      - <a href="forwardingconfiguration.md">ForwardingConfiguration</a></i>
    <a href="#redirectconfiguration" title="RedirectConfiguration">RedirectConfiguration</a>: <i>
      - <a href="redirectconfiguration.md">RedirectConfiguration</a></i>
</pre>

## Properties

#### EnforceBackendPoolsCertificateNameCheck

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FriendlyName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackendPool

_Required_: No

_Type_: List of <a href="backendpool.md">BackendPool</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackendPoolHealthProbe

_Required_: No

_Type_: List of <a href="backendpoolhealthprobe.md">BackendPoolHealthProbe</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackendPoolLoadBalancing

_Required_: No

_Type_: List of <a href="backendpoolloadbalancing.md">BackendPoolLoadBalancing</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrontendEndpoint

_Required_: No

_Type_: List of <a href="frontendendpoint.md">FrontendEndpoint</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoutingRule

_Required_: No

_Type_: List of <a href="routingrule.md">RoutingRule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backend

_Required_: No

_Type_: List of <a href="backend.md">Backend</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomHttpsConfiguration

_Required_: No

_Type_: List of <a href="customhttpsconfiguration.md">CustomHttpsConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardingConfiguration

_Required_: No

_Type_: List of <a href="forwardingconfiguration.md">ForwardingConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectConfiguration

_Required_: No

_Type_: List of <a href="redirectconfiguration.md">RedirectConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Cname

Returns the <code>Cname</code> value.

