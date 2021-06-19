# TF::Alicloud::ConfigAggregateCompliancePack

CloudFormation equivalent of alicloud_config_aggregate_compliance_pack

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::ConfigAggregateCompliancePack",
    "Properties" : {
        "<a href="#aggregatecompliancepackname" title="AggregateCompliancePackName">AggregateCompliancePackName</a>" : <i>String</i>,
        "<a href="#aggregatorid" title="AggregatorId">AggregatorId</a>" : <i>String</i>,
        "<a href="#compliancepacktemplateid" title="CompliancePackTemplateId">CompliancePackTemplateId</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#risklevel" title="RiskLevel">RiskLevel</a>" : <i>Double</i>,
        "<a href="#configrules" title="ConfigRules">ConfigRules</a>" : <i>[ <a href="configrulesdefinition.md">ConfigRulesDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::ConfigAggregateCompliancePack
Properties:
    <a href="#aggregatecompliancepackname" title="AggregateCompliancePackName">AggregateCompliancePackName</a>: <i>String</i>
    <a href="#aggregatorid" title="AggregatorId">AggregatorId</a>: <i>String</i>
    <a href="#compliancepacktemplateid" title="CompliancePackTemplateId">CompliancePackTemplateId</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#risklevel" title="RiskLevel">RiskLevel</a>: <i>Double</i>
    <a href="#configrules" title="ConfigRules">ConfigRules</a>: <i>
      - <a href="configrulesdefinition.md">ConfigRulesDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AggregateCompliancePackName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AggregatorId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompliancePackTemplateId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RiskLevel

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigRules

_Required_: No

_Type_: List of <a href="configrulesdefinition.md">ConfigRulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

#### Status

Returns the <code>Status</code> value.

