# TF::Thunder::FwGlobal

`thunder_fw_global` Provides details about thunder fw global

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::FwGlobal",
    "Properties" : {
        "<a href="#algprocessing" title="AlgProcessing">AlgProcessing</a>" : <i>String</i>,
        "<a href="#disableipfwsessions" title="DisableIpFwSessions">DisableIpFwSessions</a>" : <i>Double</i>,
        "<a href="#extendedmatching" title="ExtendedMatching">ExtendedMatching</a>" : <i>String</i>,
        "<a href="#listenonporttimeout" title="ListenOnPortTimeout">ListenOnPortTimeout</a>" : <i>Double</i>,
        "<a href="#natipddosprotection" title="NatipDdosProtection">NatipDdosProtection</a>" : <i>String</i>,
        "<a href="#permitdefaultaction" title="PermitDefaultAction">PermitDefaultAction</a>" : <i>String</i>,
        "<a href="#respondtousermac" title="RespondToUserMac">RespondToUserMac</a>" : <i>Double</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#disableapplist" title="DisableAppList">DisableAppList</a>" : <i>[ <a href="disableapplistdefinition.md">DisableAppListDefinition</a>, ... ]</i>,
        "<a href="#samplingenable" title="SamplingEnable">SamplingEnable</a>" : <i>[ <a href="samplingenabledefinition.md">SamplingEnableDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::FwGlobal
Properties:
    <a href="#algprocessing" title="AlgProcessing">AlgProcessing</a>: <i>String</i>
    <a href="#disableipfwsessions" title="DisableIpFwSessions">DisableIpFwSessions</a>: <i>Double</i>
    <a href="#extendedmatching" title="ExtendedMatching">ExtendedMatching</a>: <i>String</i>
    <a href="#listenonporttimeout" title="ListenOnPortTimeout">ListenOnPortTimeout</a>: <i>Double</i>
    <a href="#natipddosprotection" title="NatipDdosProtection">NatipDdosProtection</a>: <i>String</i>
    <a href="#permitdefaultaction" title="PermitDefaultAction">PermitDefaultAction</a>: <i>String</i>
    <a href="#respondtousermac" title="RespondToUserMac">RespondToUserMac</a>: <i>Double</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#disableapplist" title="DisableAppList">DisableAppList</a>: <i>
      - <a href="disableapplistdefinition.md">DisableAppListDefinition</a></i>
    <a href="#samplingenable" title="SamplingEnable">SamplingEnable</a>: <i>
      - <a href="samplingenabledefinition.md">SamplingEnableDefinition</a></i>
</pre>

## Properties

#### AlgProcessing

‘honor-rule-set’: Honors firewall rule-sets; ‘override-rule-set’: Override firewall rule-sets;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableIpFwSessions

disable create sessions for non TCP/UDP/ICMP.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtendedMatching

‘disable’: Disable extended matching;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ListenOnPortTimeout

STUN timeout (default: 2 minutes).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NatipDdosProtection

‘enable’: Enable; ‘disable’: Disable;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermitDefaultAction

‘forward’: Forward; ‘next-service-mode’: Service to be applied chosen based on configuration;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RespondToUserMac

Use the user’s source MAC for the next hop rather than the routing table (default: off).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableAppList

_Required_: No

_Type_: List of <a href="disableapplistdefinition.md">DisableAppListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SamplingEnable

_Required_: No

_Type_: List of <a href="samplingenabledefinition.md">SamplingEnableDefinition</a>

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

