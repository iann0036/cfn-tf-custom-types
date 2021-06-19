# TF::ACI::BridgeDomain

CloudFormation equivalent of aci_bridge_domain

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::BridgeDomain",
    "Properties" : {
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#arpflood" title="ArpFlood">ArpFlood</a>" : <i>String</i>,
        "<a href="#bridgedomaintype" title="BridgeDomainType">BridgeDomainType</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#epclear" title="EpClear">EpClear</a>" : <i>String</i>,
        "<a href="#epmovedetectmode" title="EpMoveDetectMode">EpMoveDetectMode</a>" : <i>String</i>,
        "<a href="#hostbasedrouting" title="HostBasedRouting">HostBasedRouting</a>" : <i>String</i>,
        "<a href="#intersitebumtrafficallow" title="IntersiteBumTrafficAllow">IntersiteBumTrafficAllow</a>" : <i>String</i>,
        "<a href="#intersitel2stretch" title="IntersiteL2Stretch">IntersiteL2Stretch</a>" : <i>String</i>,
        "<a href="#iplearning" title="IpLearning">IpLearning</a>" : <i>String</i>,
        "<a href="#ipv6mcastallow" title="Ipv6McastAllow">Ipv6McastAllow</a>" : <i>String</i>,
        "<a href="#limitiplearntosubnets" title="LimitIpLearnToSubnets">LimitIpLearnToSubnets</a>" : <i>String</i>,
        "<a href="#lladdr" title="LlAddr">LlAddr</a>" : <i>String</i>,
        "<a href="#mac" title="Mac">Mac</a>" : <i>String</i>,
        "<a href="#mcastallow" title="McastAllow">McastAllow</a>" : <i>String</i>,
        "<a href="#multidstpktact" title="MultiDstPktAct">MultiDstPktAct</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#optimizewanbandwidth" title="OptimizeWanBandwidth">OptimizeWanBandwidth</a>" : <i>String</i>,
        "<a href="#relationfvrsabdpolmonpol" title="RelationFvRsAbdPolMonPol">RelationFvRsAbdPolMonPol</a>" : <i>String</i>,
        "<a href="#relationfvrsbdfloodto" title="RelationFvRsBdFloodTo">RelationFvRsBdFloodTo</a>" : <i>[ String, ... ]</i>,
        "<a href="#relationfvrsbdtoepret" title="RelationFvRsBdToEpRet">RelationFvRsBdToEpRet</a>" : <i>String</i>,
        "<a href="#relationfvrsbdtofhs" title="RelationFvRsBdToFhs">RelationFvRsBdToFhs</a>" : <i>String</i>,
        "<a href="#relationfvrsbdtondp" title="RelationFvRsBdToNdP">RelationFvRsBdToNdP</a>" : <i>String</i>,
        "<a href="#relationfvrsbdtoout" title="RelationFvRsBdToOut">RelationFvRsBdToOut</a>" : <i>[ String, ... ]</i>,
        "<a href="#relationfvrsbdtoprofile" title="RelationFvRsBdToProfile">RelationFvRsBdToProfile</a>" : <i>String</i>,
        "<a href="#relationfvrsbdtorelayp" title="RelationFvRsBdToRelayP">RelationFvRsBdToRelayP</a>" : <i>String</i>,
        "<a href="#relationfvrsctx" title="RelationFvRsCtx">RelationFvRsCtx</a>" : <i>String</i>,
        "<a href="#relationfvrsigmpsn" title="RelationFvRsIgmpsn">RelationFvRsIgmpsn</a>" : <i>String</i>,
        "<a href="#relationfvrsmldsn" title="RelationFvRsMldsn">RelationFvRsMldsn</a>" : <i>String</i>,
        "<a href="#tenantdn" title="TenantDn">TenantDn</a>" : <i>String</i>,
        "<a href="#unicastroute" title="UnicastRoute">UnicastRoute</a>" : <i>String</i>,
        "<a href="#unkmacucastact" title="UnkMacUcastAct">UnkMacUcastAct</a>" : <i>String</i>,
        "<a href="#unkmcastact" title="UnkMcastAct">UnkMcastAct</a>" : <i>String</i>,
        "<a href="#v6unkmcastact" title="V6unkMcastAct">V6unkMcastAct</a>" : <i>String</i>,
        "<a href="#vmac" title="Vmac">Vmac</a>" : <i>String</i>,
        "<a href="#relationfvrsbdtonetflowmonitorpol" title="RelationFvRsBdToNetflowMonitorPol">RelationFvRsBdToNetflowMonitorPol</a>" : <i>[ <a href="relationfvrsbdtonetflowmonitorpoldefinition.md">RelationFvRsBdToNetflowMonitorPolDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::BridgeDomain
Properties:
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#arpflood" title="ArpFlood">ArpFlood</a>: <i>String</i>
    <a href="#bridgedomaintype" title="BridgeDomainType">BridgeDomainType</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#epclear" title="EpClear">EpClear</a>: <i>String</i>
    <a href="#epmovedetectmode" title="EpMoveDetectMode">EpMoveDetectMode</a>: <i>String</i>
    <a href="#hostbasedrouting" title="HostBasedRouting">HostBasedRouting</a>: <i>String</i>
    <a href="#intersitebumtrafficallow" title="IntersiteBumTrafficAllow">IntersiteBumTrafficAllow</a>: <i>String</i>
    <a href="#intersitel2stretch" title="IntersiteL2Stretch">IntersiteL2Stretch</a>: <i>String</i>
    <a href="#iplearning" title="IpLearning">IpLearning</a>: <i>String</i>
    <a href="#ipv6mcastallow" title="Ipv6McastAllow">Ipv6McastAllow</a>: <i>String</i>
    <a href="#limitiplearntosubnets" title="LimitIpLearnToSubnets">LimitIpLearnToSubnets</a>: <i>String</i>
    <a href="#lladdr" title="LlAddr">LlAddr</a>: <i>String</i>
    <a href="#mac" title="Mac">Mac</a>: <i>String</i>
    <a href="#mcastallow" title="McastAllow">McastAllow</a>: <i>String</i>
    <a href="#multidstpktact" title="MultiDstPktAct">MultiDstPktAct</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#optimizewanbandwidth" title="OptimizeWanBandwidth">OptimizeWanBandwidth</a>: <i>String</i>
    <a href="#relationfvrsabdpolmonpol" title="RelationFvRsAbdPolMonPol">RelationFvRsAbdPolMonPol</a>: <i>String</i>
    <a href="#relationfvrsbdfloodto" title="RelationFvRsBdFloodTo">RelationFvRsBdFloodTo</a>: <i>
      - String</i>
    <a href="#relationfvrsbdtoepret" title="RelationFvRsBdToEpRet">RelationFvRsBdToEpRet</a>: <i>String</i>
    <a href="#relationfvrsbdtofhs" title="RelationFvRsBdToFhs">RelationFvRsBdToFhs</a>: <i>String</i>
    <a href="#relationfvrsbdtondp" title="RelationFvRsBdToNdP">RelationFvRsBdToNdP</a>: <i>String</i>
    <a href="#relationfvrsbdtoout" title="RelationFvRsBdToOut">RelationFvRsBdToOut</a>: <i>
      - String</i>
    <a href="#relationfvrsbdtoprofile" title="RelationFvRsBdToProfile">RelationFvRsBdToProfile</a>: <i>String</i>
    <a href="#relationfvrsbdtorelayp" title="RelationFvRsBdToRelayP">RelationFvRsBdToRelayP</a>: <i>String</i>
    <a href="#relationfvrsctx" title="RelationFvRsCtx">RelationFvRsCtx</a>: <i>String</i>
    <a href="#relationfvrsigmpsn" title="RelationFvRsIgmpsn">RelationFvRsIgmpsn</a>: <i>String</i>
    <a href="#relationfvrsmldsn" title="RelationFvRsMldsn">RelationFvRsMldsn</a>: <i>String</i>
    <a href="#tenantdn" title="TenantDn">TenantDn</a>: <i>String</i>
    <a href="#unicastroute" title="UnicastRoute">UnicastRoute</a>: <i>String</i>
    <a href="#unkmacucastact" title="UnkMacUcastAct">UnkMacUcastAct</a>: <i>String</i>
    <a href="#unkmcastact" title="UnkMcastAct">UnkMcastAct</a>: <i>String</i>
    <a href="#v6unkmcastact" title="V6unkMcastAct">V6unkMcastAct</a>: <i>String</i>
    <a href="#vmac" title="Vmac">Vmac</a>: <i>String</i>
    <a href="#relationfvrsbdtonetflowmonitorpol" title="RelationFvRsBdToNetflowMonitorPol">RelationFvRsBdToNetflowMonitorPol</a>: <i>
      - <a href="relationfvrsbdtonetflowmonitorpoldefinition.md">RelationFvRsBdToNetflowMonitorPolDefinition</a></i>
</pre>

## Properties

#### Annotation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ArpFlood

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BridgeDomainType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EpClear

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EpMoveDetectMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostBasedRouting

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntersiteBumTrafficAllow

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntersiteL2Stretch

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpLearning

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6McastAllow

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LimitIpLearnToSubnets

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LlAddr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mac

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### McastAllow

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MultiDstPktAct

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameAlias

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OptimizeWanBandwidth

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsAbdPolMonPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsBdFloodTo

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsBdToEpRet

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsBdToFhs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsBdToNdP

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsBdToOut

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsBdToProfile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsBdToRelayP

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsCtx

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsIgmpsn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsMldsn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantDn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnicastRoute

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnkMacUcastAct

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnkMcastAct

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### V6unkMcastAct

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vmac

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsBdToNetflowMonitorPol

_Required_: No

_Type_: List of <a href="relationfvrsbdtonetflowmonitorpoldefinition.md">RelationFvRsBdToNetflowMonitorPolDefinition</a>

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

