# TF::ACI::ServiceRedirectPolicy

CloudFormation equivalent of aci_service_redirect_policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::ServiceRedirectPolicy",
    "Properties" : {
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#anycastenabled" title="AnycastEnabled">AnycastEnabled</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#desttype" title="DestType">DestType</a>" : <i>String</i>,
        "<a href="#hashingalgorithm" title="HashingAlgorithm">HashingAlgorithm</a>" : <i>String</i>,
        "<a href="#maxthresholdpercent" title="MaxThresholdPercent">MaxThresholdPercent</a>" : <i>String</i>,
        "<a href="#minthresholdpercent" title="MinThresholdPercent">MinThresholdPercent</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#programlocalpodonly" title="ProgramLocalPodOnly">ProgramLocalPodOnly</a>" : <i>String</i>,
        "<a href="#relationvnsrsipslamonitoringpol" title="RelationVnsRsIpslaMonitoringPol">RelationVnsRsIpslaMonitoringPol</a>" : <i>String</i>,
        "<a href="#resilienthashenabled" title="ResilientHashEnabled">ResilientHashEnabled</a>" : <i>String</i>,
        "<a href="#tenantdn" title="TenantDn">TenantDn</a>" : <i>String</i>,
        "<a href="#thresholddownaction" title="ThresholdDownAction">ThresholdDownAction</a>" : <i>String</i>,
        "<a href="#thresholdenable" title="ThresholdEnable">ThresholdEnable</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::ServiceRedirectPolicy
Properties:
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#anycastenabled" title="AnycastEnabled">AnycastEnabled</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#desttype" title="DestType">DestType</a>: <i>String</i>
    <a href="#hashingalgorithm" title="HashingAlgorithm">HashingAlgorithm</a>: <i>String</i>
    <a href="#maxthresholdpercent" title="MaxThresholdPercent">MaxThresholdPercent</a>: <i>String</i>
    <a href="#minthresholdpercent" title="MinThresholdPercent">MinThresholdPercent</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#programlocalpodonly" title="ProgramLocalPodOnly">ProgramLocalPodOnly</a>: <i>String</i>
    <a href="#relationvnsrsipslamonitoringpol" title="RelationVnsRsIpslaMonitoringPol">RelationVnsRsIpslaMonitoringPol</a>: <i>String</i>
    <a href="#resilienthashenabled" title="ResilientHashEnabled">ResilientHashEnabled</a>: <i>String</i>
    <a href="#tenantdn" title="TenantDn">TenantDn</a>: <i>String</i>
    <a href="#thresholddownaction" title="ThresholdDownAction">ThresholdDownAction</a>: <i>String</i>
    <a href="#thresholdenable" title="ThresholdEnable">ThresholdEnable</a>: <i>String</i>
</pre>

## Properties

#### Annotation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AnycastEnabled

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HashingAlgorithm

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxThresholdPercent

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinThresholdPercent

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

#### ProgramLocalPodOnly

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVnsRsIpslaMonitoringPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResilientHashEnabled

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantDn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThresholdDownAction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThresholdEnable

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

