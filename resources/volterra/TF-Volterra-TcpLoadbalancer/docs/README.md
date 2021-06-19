# TF::Volterra::TcpLoadbalancer

CloudFormation equivalent of volterra_tcp_loadbalancer

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Volterra::TcpLoadbalancer",
    "Properties" : {
        "<a href="#advertiseonpublicdefaultvip" title="AdvertiseOnPublicDefaultVip">AdvertiseOnPublicDefaultVip</a>" : <i>Boolean</i>,
        "<a href="#annotations" title="Annotations">Annotations</a>" : <i>[ <a href="annotationsdefinition.md">AnnotationsDefinition</a>, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#disable" title="Disable">Disable</a>" : <i>Boolean</i>,
        "<a href="#dnsvolterramanaged" title="DnsVolterraManaged">DnsVolterraManaged</a>" : <i>Boolean</i>,
        "<a href="#donotadvertise" title="DoNotAdvertise">DoNotAdvertise</a>" : <i>Boolean</i>,
        "<a href="#donotretractcluster" title="DoNotRetractCluster">DoNotRetractCluster</a>" : <i>Boolean</i>,
        "<a href="#domains" title="Domains">Domains</a>" : <i>[ String, ... ]</i>,
        "<a href="#hashpolicychoiceleastactive" title="HashPolicyChoiceLeastActive">HashPolicyChoiceLeastActive</a>" : <i>Boolean</i>,
        "<a href="#hashpolicychoicerandom" title="HashPolicyChoiceRandom">HashPolicyChoiceRandom</a>" : <i>Boolean</i>,
        "<a href="#hashpolicychoiceroundrobin" title="HashPolicyChoiceRoundRobin">HashPolicyChoiceRoundRobin</a>" : <i>Boolean</i>,
        "<a href="#hashpolicychoicesourceipstickiness" title="HashPolicyChoiceSourceIpStickiness">HashPolicyChoiceSourceIpStickiness</a>" : <i>Boolean</i>,
        "<a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>" : <i>Double</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#listenport" title="ListenPort">ListenPort</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
        "<a href="#retractcluster" title="RetractCluster">RetractCluster</a>" : <i>Boolean</i>,
        "<a href="#withsni" title="WithSni">WithSni</a>" : <i>Boolean</i>,
        "<a href="#advertisecustom" title="AdvertiseCustom">AdvertiseCustom</a>" : <i>[ <a href="advertisecustomdefinition.md">AdvertiseCustomDefinition</a>, ... ]</i>,
        "<a href="#advertiseonpublic" title="AdvertiseOnPublic">AdvertiseOnPublic</a>" : <i>[ <a href="advertiseonpublicdefinition.md">AdvertiseOnPublicDefinition</a>, ... ]</i>,
        "<a href="#originpoolsweights" title="OriginPoolsWeights">OriginPoolsWeights</a>" : <i>[ <a href="originpoolsweightsdefinition.md">OriginPoolsWeightsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Volterra::TcpLoadbalancer
Properties:
    <a href="#advertiseonpublicdefaultvip" title="AdvertiseOnPublicDefaultVip">AdvertiseOnPublicDefaultVip</a>: <i>Boolean</i>
    <a href="#annotations" title="Annotations">Annotations</a>: <i>
      - <a href="annotationsdefinition.md">AnnotationsDefinition</a></i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#disable" title="Disable">Disable</a>: <i>Boolean</i>
    <a href="#dnsvolterramanaged" title="DnsVolterraManaged">DnsVolterraManaged</a>: <i>Boolean</i>
    <a href="#donotadvertise" title="DoNotAdvertise">DoNotAdvertise</a>: <i>Boolean</i>
    <a href="#donotretractcluster" title="DoNotRetractCluster">DoNotRetractCluster</a>: <i>Boolean</i>
    <a href="#domains" title="Domains">Domains</a>: <i>
      - String</i>
    <a href="#hashpolicychoiceleastactive" title="HashPolicyChoiceLeastActive">HashPolicyChoiceLeastActive</a>: <i>Boolean</i>
    <a href="#hashpolicychoicerandom" title="HashPolicyChoiceRandom">HashPolicyChoiceRandom</a>: <i>Boolean</i>
    <a href="#hashpolicychoiceroundrobin" title="HashPolicyChoiceRoundRobin">HashPolicyChoiceRoundRobin</a>: <i>Boolean</i>
    <a href="#hashpolicychoicesourceipstickiness" title="HashPolicyChoiceSourceIpStickiness">HashPolicyChoiceSourceIpStickiness</a>: <i>Boolean</i>
    <a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>: <i>Double</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#listenport" title="ListenPort">ListenPort</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
    <a href="#retractcluster" title="RetractCluster">RetractCluster</a>: <i>Boolean</i>
    <a href="#withsni" title="WithSni">WithSni</a>: <i>Boolean</i>
    <a href="#advertisecustom" title="AdvertiseCustom">AdvertiseCustom</a>: <i>
      - <a href="advertisecustomdefinition.md">AdvertiseCustomDefinition</a></i>
    <a href="#advertiseonpublic" title="AdvertiseOnPublic">AdvertiseOnPublic</a>: <i>
      - <a href="advertiseonpublicdefinition.md">AdvertiseOnPublicDefinition</a></i>
    <a href="#originpoolsweights" title="OriginPoolsWeights">OriginPoolsWeights</a>: <i>
      - <a href="originpoolsweightsdefinition.md">OriginPoolsWeightsDefinition</a></i>
</pre>

## Properties

#### AdvertiseOnPublicDefaultVip

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Annotations

_Required_: No

_Type_: List of <a href="annotationsdefinition.md">AnnotationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsVolterraManaged

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DoNotAdvertise

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DoNotRetractCluster

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domains

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HashPolicyChoiceLeastActive

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HashPolicyChoiceRandom

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HashPolicyChoiceRoundRobin

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HashPolicyChoiceSourceIpStickiness

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdleTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ListenPort

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetractCluster

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WithSni

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvertiseCustom

_Required_: No

_Type_: List of <a href="advertisecustomdefinition.md">AdvertiseCustomDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvertiseOnPublic

_Required_: No

_Type_: List of <a href="advertiseonpublicdefinition.md">AdvertiseOnPublicDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginPoolsWeights

_Required_: No

_Type_: List of <a href="originpoolsweightsdefinition.md">OriginPoolsWeightsDefinition</a>

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

