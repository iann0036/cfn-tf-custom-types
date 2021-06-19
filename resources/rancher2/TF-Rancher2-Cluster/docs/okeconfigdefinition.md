# TF::Rancher2::Cluster OkeConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
    "<a href="#custombootvolumesize" title="CustomBootVolumeSize">CustomBootVolumeSize</a>" : <i>Double</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#enablekubernetesdashboard" title="EnableKubernetesDashboard">EnableKubernetesDashboard</a>" : <i>Boolean</i>,
    "<a href="#enableprivatenodes" title="EnablePrivateNodes">EnablePrivateNodes</a>" : <i>Boolean</i>,
    "<a href="#fingerprint" title="Fingerprint">Fingerprint</a>" : <i>String</i>,
    "<a href="#flexocpus" title="FlexOcpus">FlexOcpus</a>" : <i>Double</i>,
    "<a href="#kubernetesversion" title="KubernetesVersion">KubernetesVersion</a>" : <i>String</i>,
    "<a href="#limitnodecount" title="LimitNodeCount">LimitNodeCount</a>" : <i>Double</i>,
    "<a href="#loadbalancersubnetname1" title="LoadBalancerSubnetName1">LoadBalancerSubnetName1</a>" : <i>String</i>,
    "<a href="#loadbalancersubnetname2" title="LoadBalancerSubnetName2">LoadBalancerSubnetName2</a>" : <i>String</i>,
    "<a href="#nodeimage" title="NodeImage">NodeImage</a>" : <i>String</i>,
    "<a href="#nodepooldnsdomainname" title="NodePoolDnsDomainName">NodePoolDnsDomainName</a>" : <i>String</i>,
    "<a href="#nodepoolsubnetname" title="NodePoolSubnetName">NodePoolSubnetName</a>" : <i>String</i>,
    "<a href="#nodepublickeycontents" title="NodePublicKeyContents">NodePublicKeyContents</a>" : <i>String</i>,
    "<a href="#nodeshape" title="NodeShape">NodeShape</a>" : <i>String</i>,
    "<a href="#podcidr" title="PodCidr">PodCidr</a>" : <i>String</i>,
    "<a href="#privatekeycontents" title="PrivateKeyContents">PrivateKeyContents</a>" : <i>String</i>,
    "<a href="#privatekeypassphrase" title="PrivateKeyPassphrase">PrivateKeyPassphrase</a>" : <i>String</i>,
    "<a href="#quantityofnodesubnets" title="QuantityOfNodeSubnets">QuantityOfNodeSubnets</a>" : <i>Double</i>,
    "<a href="#quantitypersubnet" title="QuantityPerSubnet">QuantityPerSubnet</a>" : <i>Double</i>,
    "<a href="#region" title="Region">Region</a>" : <i>String</i>,
    "<a href="#servicecidr" title="ServiceCidr">ServiceCidr</a>" : <i>String</i>,
    "<a href="#servicednsdomainname" title="ServiceDnsDomainName">ServiceDnsDomainName</a>" : <i>String</i>,
    "<a href="#skipvcndelete" title="SkipVcnDelete">SkipVcnDelete</a>" : <i>Boolean</i>,
    "<a href="#tenancyid" title="TenancyId">TenancyId</a>" : <i>String</i>,
    "<a href="#userocid" title="UserOcid">UserOcid</a>" : <i>String</i>,
    "<a href="#vcncompartmentid" title="VcnCompartmentId">VcnCompartmentId</a>" : <i>String</i>,
    "<a href="#vcnname" title="VcnName">VcnName</a>" : <i>String</i>,
    "<a href="#workernodeingresscidr" title="WorkerNodeIngressCidr">WorkerNodeIngressCidr</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
<a href="#custombootvolumesize" title="CustomBootVolumeSize">CustomBootVolumeSize</a>: <i>Double</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#enablekubernetesdashboard" title="EnableKubernetesDashboard">EnableKubernetesDashboard</a>: <i>Boolean</i>
<a href="#enableprivatenodes" title="EnablePrivateNodes">EnablePrivateNodes</a>: <i>Boolean</i>
<a href="#fingerprint" title="Fingerprint">Fingerprint</a>: <i>String</i>
<a href="#flexocpus" title="FlexOcpus">FlexOcpus</a>: <i>Double</i>
<a href="#kubernetesversion" title="KubernetesVersion">KubernetesVersion</a>: <i>String</i>
<a href="#limitnodecount" title="LimitNodeCount">LimitNodeCount</a>: <i>Double</i>
<a href="#loadbalancersubnetname1" title="LoadBalancerSubnetName1">LoadBalancerSubnetName1</a>: <i>String</i>
<a href="#loadbalancersubnetname2" title="LoadBalancerSubnetName2">LoadBalancerSubnetName2</a>: <i>String</i>
<a href="#nodeimage" title="NodeImage">NodeImage</a>: <i>String</i>
<a href="#nodepooldnsdomainname" title="NodePoolDnsDomainName">NodePoolDnsDomainName</a>: <i>String</i>
<a href="#nodepoolsubnetname" title="NodePoolSubnetName">NodePoolSubnetName</a>: <i>String</i>
<a href="#nodepublickeycontents" title="NodePublicKeyContents">NodePublicKeyContents</a>: <i>String</i>
<a href="#nodeshape" title="NodeShape">NodeShape</a>: <i>String</i>
<a href="#podcidr" title="PodCidr">PodCidr</a>: <i>String</i>
<a href="#privatekeycontents" title="PrivateKeyContents">PrivateKeyContents</a>: <i>String</i>
<a href="#privatekeypassphrase" title="PrivateKeyPassphrase">PrivateKeyPassphrase</a>: <i>String</i>
<a href="#quantityofnodesubnets" title="QuantityOfNodeSubnets">QuantityOfNodeSubnets</a>: <i>Double</i>
<a href="#quantitypersubnet" title="QuantityPerSubnet">QuantityPerSubnet</a>: <i>Double</i>
<a href="#region" title="Region">Region</a>: <i>String</i>
<a href="#servicecidr" title="ServiceCidr">ServiceCidr</a>: <i>String</i>
<a href="#servicednsdomainname" title="ServiceDnsDomainName">ServiceDnsDomainName</a>: <i>String</i>
<a href="#skipvcndelete" title="SkipVcnDelete">SkipVcnDelete</a>: <i>Boolean</i>
<a href="#tenancyid" title="TenancyId">TenancyId</a>: <i>String</i>
<a href="#userocid" title="UserOcid">UserOcid</a>: <i>String</i>
<a href="#vcncompartmentid" title="VcnCompartmentId">VcnCompartmentId</a>: <i>String</i>
<a href="#vcnname" title="VcnName">VcnName</a>: <i>String</i>
<a href="#workernodeingresscidr" title="WorkerNodeIngressCidr">WorkerNodeIngressCidr</a>: <i>String</i>
</pre>

## Properties

#### CompartmentId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomBootVolumeSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableKubernetesDashboard

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnablePrivateNodes

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fingerprint

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlexOcpus

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesVersion

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LimitNodeCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerSubnetName1

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerSubnetName2

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeImage

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodePoolDnsDomainName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodePoolSubnetName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodePublicKeyContents

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeShape

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PodCidr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateKeyContents

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateKeyPassphrase

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuantityOfNodeSubnets

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuantityPerSubnet

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceCidr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceDnsDomainName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipVcnDelete

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenancyId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserOcid

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VcnCompartmentId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VcnName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerNodeIngressCidr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

