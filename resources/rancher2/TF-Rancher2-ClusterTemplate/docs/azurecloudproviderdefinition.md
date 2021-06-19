# TF::Rancher2::ClusterTemplate AzureCloudProviderDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#aadclientcertpassword" title="AadClientCertPassword">AadClientCertPassword</a>" : <i>String</i>,
    "<a href="#aadclientcertpath" title="AadClientCertPath">AadClientCertPath</a>" : <i>String</i>,
    "<a href="#aadclientid" title="AadClientId">AadClientId</a>" : <i>String</i>,
    "<a href="#aadclientsecret" title="AadClientSecret">AadClientSecret</a>" : <i>String</i>,
    "<a href="#cloud" title="Cloud">Cloud</a>" : <i>String</i>,
    "<a href="#cloudproviderbackoff" title="CloudProviderBackoff">CloudProviderBackoff</a>" : <i>Boolean</i>,
    "<a href="#cloudproviderbackoffduration" title="CloudProviderBackoffDuration">CloudProviderBackoffDuration</a>" : <i>Double</i>,
    "<a href="#cloudproviderbackoffexponent" title="CloudProviderBackoffExponent">CloudProviderBackoffExponent</a>" : <i>Double</i>,
    "<a href="#cloudproviderbackoffjitter" title="CloudProviderBackoffJitter">CloudProviderBackoffJitter</a>" : <i>Double</i>,
    "<a href="#cloudproviderbackoffretries" title="CloudProviderBackoffRetries">CloudProviderBackoffRetries</a>" : <i>Double</i>,
    "<a href="#cloudproviderratelimit" title="CloudProviderRateLimit">CloudProviderRateLimit</a>" : <i>Boolean</i>,
    "<a href="#cloudproviderratelimitbucket" title="CloudProviderRateLimitBucket">CloudProviderRateLimitBucket</a>" : <i>Double</i>,
    "<a href="#cloudproviderratelimitqps" title="CloudProviderRateLimitQps">CloudProviderRateLimitQps</a>" : <i>Double</i>,
    "<a href="#loadbalancersku" title="LoadBalancerSku">LoadBalancerSku</a>" : <i>String</i>,
    "<a href="#location" title="Location">Location</a>" : <i>String</i>,
    "<a href="#maximumloadbalancerrulecount" title="MaximumLoadBalancerRuleCount">MaximumLoadBalancerRuleCount</a>" : <i>Double</i>,
    "<a href="#primaryavailabilitysetname" title="PrimaryAvailabilitySetName">PrimaryAvailabilitySetName</a>" : <i>String</i>,
    "<a href="#primaryscalesetname" title="PrimaryScaleSetName">PrimaryScaleSetName</a>" : <i>String</i>,
    "<a href="#resourcegroup" title="ResourceGroup">ResourceGroup</a>" : <i>String</i>,
    "<a href="#routetablename" title="RouteTableName">RouteTableName</a>" : <i>String</i>,
    "<a href="#securitygroupname" title="SecurityGroupName">SecurityGroupName</a>" : <i>String</i>,
    "<a href="#subnetname" title="SubnetName">SubnetName</a>" : <i>String</i>,
    "<a href="#subscriptionid" title="SubscriptionId">SubscriptionId</a>" : <i>String</i>,
    "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>,
    "<a href="#useinstancemetadata" title="UseInstanceMetadata">UseInstanceMetadata</a>" : <i>Boolean</i>,
    "<a href="#usemanagedidentityextension" title="UseManagedIdentityExtension">UseManagedIdentityExtension</a>" : <i>Boolean</i>,
    "<a href="#vmtype" title="VmType">VmType</a>" : <i>String</i>,
    "<a href="#vnetname" title="VnetName">VnetName</a>" : <i>String</i>,
    "<a href="#vnetresourcegroup" title="VnetResourceGroup">VnetResourceGroup</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#aadclientcertpassword" title="AadClientCertPassword">AadClientCertPassword</a>: <i>String</i>
<a href="#aadclientcertpath" title="AadClientCertPath">AadClientCertPath</a>: <i>String</i>
<a href="#aadclientid" title="AadClientId">AadClientId</a>: <i>String</i>
<a href="#aadclientsecret" title="AadClientSecret">AadClientSecret</a>: <i>String</i>
<a href="#cloud" title="Cloud">Cloud</a>: <i>String</i>
<a href="#cloudproviderbackoff" title="CloudProviderBackoff">CloudProviderBackoff</a>: <i>Boolean</i>
<a href="#cloudproviderbackoffduration" title="CloudProviderBackoffDuration">CloudProviderBackoffDuration</a>: <i>Double</i>
<a href="#cloudproviderbackoffexponent" title="CloudProviderBackoffExponent">CloudProviderBackoffExponent</a>: <i>Double</i>
<a href="#cloudproviderbackoffjitter" title="CloudProviderBackoffJitter">CloudProviderBackoffJitter</a>: <i>Double</i>
<a href="#cloudproviderbackoffretries" title="CloudProviderBackoffRetries">CloudProviderBackoffRetries</a>: <i>Double</i>
<a href="#cloudproviderratelimit" title="CloudProviderRateLimit">CloudProviderRateLimit</a>: <i>Boolean</i>
<a href="#cloudproviderratelimitbucket" title="CloudProviderRateLimitBucket">CloudProviderRateLimitBucket</a>: <i>Double</i>
<a href="#cloudproviderratelimitqps" title="CloudProviderRateLimitQps">CloudProviderRateLimitQps</a>: <i>Double</i>
<a href="#loadbalancersku" title="LoadBalancerSku">LoadBalancerSku</a>: <i>String</i>
<a href="#location" title="Location">Location</a>: <i>String</i>
<a href="#maximumloadbalancerrulecount" title="MaximumLoadBalancerRuleCount">MaximumLoadBalancerRuleCount</a>: <i>Double</i>
<a href="#primaryavailabilitysetname" title="PrimaryAvailabilitySetName">PrimaryAvailabilitySetName</a>: <i>String</i>
<a href="#primaryscalesetname" title="PrimaryScaleSetName">PrimaryScaleSetName</a>: <i>String</i>
<a href="#resourcegroup" title="ResourceGroup">ResourceGroup</a>: <i>String</i>
<a href="#routetablename" title="RouteTableName">RouteTableName</a>: <i>String</i>
<a href="#securitygroupname" title="SecurityGroupName">SecurityGroupName</a>: <i>String</i>
<a href="#subnetname" title="SubnetName">SubnetName</a>: <i>String</i>
<a href="#subscriptionid" title="SubscriptionId">SubscriptionId</a>: <i>String</i>
<a href="#tenantid" title="TenantId">TenantId</a>: <i>String</i>
<a href="#useinstancemetadata" title="UseInstanceMetadata">UseInstanceMetadata</a>: <i>Boolean</i>
<a href="#usemanagedidentityextension" title="UseManagedIdentityExtension">UseManagedIdentityExtension</a>: <i>Boolean</i>
<a href="#vmtype" title="VmType">VmType</a>: <i>String</i>
<a href="#vnetname" title="VnetName">VnetName</a>: <i>String</i>
<a href="#vnetresourcegroup" title="VnetResourceGroup">VnetResourceGroup</a>: <i>String</i>
</pre>

## Properties

#### AadClientCertPassword

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AadClientCertPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AadClientId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AadClientSecret

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cloud

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudProviderBackoff

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudProviderBackoffDuration

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudProviderBackoffExponent

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudProviderBackoffJitter

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudProviderBackoffRetries

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudProviderRateLimit

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudProviderRateLimitBucket

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudProviderRateLimitQps

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerSku

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumLoadBalancerRuleCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryAvailabilitySetName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryScaleSetName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteTableName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubscriptionId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseInstanceMetadata

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseManagedIdentityExtension

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VnetName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VnetResourceGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

