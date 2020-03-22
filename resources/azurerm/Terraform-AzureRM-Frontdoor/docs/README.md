# Terraform::AzureRM::Frontdoor

Manages an Azure Front Door instance.

Azure Front Door Service is Microsoft's highly available and scalable web application acceleration platform and global HTTP(s) load balancer. It provides built-in DDoS protection and application layer security and caching. Front Door enables you to build applications that maximize and automate high-availability and performance for your end-users. Use Front Door with Azure services including Web/Mobile Apps, Cloud Services and Virtual Machines – or combine it with on-premises services for hybrid deployments and smooth cloud migration.

Below are some of the key scenarios that Azure Front Door Service addresses:
* Use Front Door to improve application scale and availability with instant multi-region failover
* Use Front Door to improve application performance with SSL offload and routing requests to the fastest available application backend.
* Use Front Door for application layer security and DDoS protection for your application.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::Frontdoor",
    "Properties" : {
        "<a href="#enforcebackendpoolscertificatenamecheck" title="EnforceBackendPoolsCertificateNameCheck">EnforceBackendPoolsCertificateNameCheck</a>" : <i>Boolean</i>,
        "<a href="#friendlyname" title="FriendlyName">FriendlyName</a>" : <i>String</i>,
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

Enforce certificate name check on `HTTPS` requests to all backend pools, this setting will have no effect on `HTTP` requests. Permitted values are `true` or `false`.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FriendlyName

A friendly name for the Front Door service.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerEnabled

Should the Front Door Load Balancer be Enabled? Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the Front Door service. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

Specifies the name of the Resource Group in which the Front Door service should exist. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

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

#### Id

Returns the <code>Id</code> value.

