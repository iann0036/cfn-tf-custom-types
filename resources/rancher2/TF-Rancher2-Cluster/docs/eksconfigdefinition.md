# TF::Rancher2::Cluster EksConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accesskey" title="AccessKey">AccessKey</a>" : <i>String</i>,
    "<a href="#ami" title="Ami">Ami</a>" : <i>String</i>,
    "<a href="#associateworkernodepublicip" title="AssociateWorkerNodePublicIp">AssociateWorkerNodePublicIp</a>" : <i>Boolean</i>,
    "<a href="#desirednodes" title="DesiredNodes">DesiredNodes</a>" : <i>Double</i>,
    "<a href="#ebsencryption" title="EbsEncryption">EbsEncryption</a>" : <i>Boolean</i>,
    "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
    "<a href="#keypairname" title="KeyPairName">KeyPairName</a>" : <i>String</i>,
    "<a href="#kubernetesversion" title="KubernetesVersion">KubernetesVersion</a>" : <i>String</i>,
    "<a href="#maximumnodes" title="MaximumNodes">MaximumNodes</a>" : <i>Double</i>,
    "<a href="#minimumnodes" title="MinimumNodes">MinimumNodes</a>" : <i>Double</i>,
    "<a href="#nodevolumesize" title="NodeVolumeSize">NodeVolumeSize</a>" : <i>Double</i>,
    "<a href="#region" title="Region">Region</a>" : <i>String</i>,
    "<a href="#secretkey" title="SecretKey">SecretKey</a>" : <i>String</i>,
    "<a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>" : <i>[ String, ... ]</i>,
    "<a href="#servicerole" title="ServiceRole">ServiceRole</a>" : <i>String</i>,
    "<a href="#sessiontoken" title="SessionToken">SessionToken</a>" : <i>String</i>,
    "<a href="#subnets" title="Subnets">Subnets</a>" : <i>[ String, ... ]</i>,
    "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
    "<a href="#virtualnetwork" title="VirtualNetwork">VirtualNetwork</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#accesskey" title="AccessKey">AccessKey</a>: <i>String</i>
<a href="#ami" title="Ami">Ami</a>: <i>String</i>
<a href="#associateworkernodepublicip" title="AssociateWorkerNodePublicIp">AssociateWorkerNodePublicIp</a>: <i>Boolean</i>
<a href="#desirednodes" title="DesiredNodes">DesiredNodes</a>: <i>Double</i>
<a href="#ebsencryption" title="EbsEncryption">EbsEncryption</a>: <i>Boolean</i>
<a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
<a href="#keypairname" title="KeyPairName">KeyPairName</a>: <i>String</i>
<a href="#kubernetesversion" title="KubernetesVersion">KubernetesVersion</a>: <i>String</i>
<a href="#maximumnodes" title="MaximumNodes">MaximumNodes</a>: <i>Double</i>
<a href="#minimumnodes" title="MinimumNodes">MinimumNodes</a>: <i>Double</i>
<a href="#nodevolumesize" title="NodeVolumeSize">NodeVolumeSize</a>: <i>Double</i>
<a href="#region" title="Region">Region</a>: <i>String</i>
<a href="#secretkey" title="SecretKey">SecretKey</a>: <i>String</i>
<a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>: <i>
      - String</i>
<a href="#servicerole" title="ServiceRole">ServiceRole</a>: <i>String</i>
<a href="#sessiontoken" title="SessionToken">SessionToken</a>: <i>String</i>
<a href="#subnets" title="Subnets">Subnets</a>: <i>
      - String</i>
<a href="#userdata" title="UserData">UserData</a>: <i>String</i>
<a href="#virtualnetwork" title="VirtualNetwork">VirtualNetwork</a>: <i>String</i>
</pre>

## Properties

#### AccessKey

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ami

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssociateWorkerNodePublicIp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesiredNodes

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsEncryption

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyPairName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesVersion

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumNodes

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinimumNodes

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeVolumeSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretKey

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroups

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceRole

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionToken

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnets

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualNetwork

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

