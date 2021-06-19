# TF::AzureRM::SecurityCenterAssessment

Manages the Security Center Assessment for Azure Security Center.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::SecurityCenterAssessment",
    "Properties" : {
        "<a href="#additionaldata" title="AdditionalData">AdditionalData</a>" : <i>[ <a href="additionaldatadefinition.md">AdditionalDataDefinition</a>, ... ]</i>,
        "<a href="#assessmentpolicyid" title="AssessmentPolicyId">AssessmentPolicyId</a>" : <i>String</i>,
        "<a href="#targetresourceid" title="TargetResourceId">TargetResourceId</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>[ <a href="statusdefinition.md">StatusDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::SecurityCenterAssessment
Properties:
    <a href="#additionaldata" title="AdditionalData">AdditionalData</a>: <i>
      - <a href="additionaldatadefinition.md">AdditionalDataDefinition</a></i>
    <a href="#assessmentpolicyid" title="AssessmentPolicyId">AssessmentPolicyId</a>: <i>String</i>
    <a href="#targetresourceid" title="TargetResourceId">TargetResourceId</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>
      - <a href="statusdefinition.md">StatusDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AdditionalData

_Required_: No

_Type_: List of <a href="additionaldatadefinition.md">AdditionalDataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssessmentPolicyId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetResourceId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: List of <a href="statusdefinition.md">StatusDefinition</a>

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

