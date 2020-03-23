# Terraform::AWS::SsmAssociation

Associates an SSM Document to an instance or EC2 tag.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::SsmAssociation",
    "Properties" : {
        "<a href="#associationname" title="AssociationName">AssociationName</a>" : <i>String</i>,
        "<a href="#automationtargetparametername" title="AutomationTargetParameterName">AutomationTargetParameterName</a>" : <i>String</i>,
        "<a href="#complianceseverity" title="ComplianceSeverity">ComplianceSeverity</a>" : <i>String</i>,
        "<a href="#documentversion" title="DocumentVersion">DocumentVersion</a>" : <i>String</i>,
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
        "<a href="#maxconcurrency" title="MaxConcurrency">MaxConcurrency</a>" : <i>String</i>,
        "<a href="#maxerrors" title="MaxErrors">MaxErrors</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#parameters" title="Parameters">Parameters</a>" : <i>[ <a href="parameters.md">Parameters</a>, ... ]</i>,
        "<a href="#scheduleexpression" title="ScheduleExpression">ScheduleExpression</a>" : <i>String</i>,
        "<a href="#outputlocation" title="OutputLocation">OutputLocation</a>" : <i>[ <a href="outputlocation.md">OutputLocation</a>, ... ]</i>,
        "<a href="#targets" title="Targets">Targets</a>" : <i>[ <a href="targets.md">Targets</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::SsmAssociation
Properties:
    <a href="#associationname" title="AssociationName">AssociationName</a>: <i>String</i>
    <a href="#automationtargetparametername" title="AutomationTargetParameterName">AutomationTargetParameterName</a>: <i>String</i>
    <a href="#complianceseverity" title="ComplianceSeverity">ComplianceSeverity</a>: <i>String</i>
    <a href="#documentversion" title="DocumentVersion">DocumentVersion</a>: <i>String</i>
    <a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
    <a href="#maxconcurrency" title="MaxConcurrency">MaxConcurrency</a>: <i>String</i>
    <a href="#maxerrors" title="MaxErrors">MaxErrors</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#parameters" title="Parameters">Parameters</a>: <i>
      - <a href="parameters.md">Parameters</a></i>
    <a href="#scheduleexpression" title="ScheduleExpression">ScheduleExpression</a>: <i>String</i>
    <a href="#outputlocation" title="OutputLocation">OutputLocation</a>: <i>
      - <a href="outputlocation.md">OutputLocation</a></i>
    <a href="#targets" title="Targets">Targets</a>: <i>
      - <a href="targets.md">Targets</a></i>
</pre>

## Properties

#### AssociationName

The descriptive name for the association.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutomationTargetParameterName

Specify the target for the association. This target is required for associations that use an `Automation` document and target resources by using rate controls.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComplianceSeverity

The compliance severity for the association. Can be one of the following: `UNSPECIFIED`, `LOW`, `MEDIUM`, `HIGH` or `CRITICAL`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DocumentVersion

The document version you want to associate with the target(s). Can be a specific version or the default version.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceId

The instance ID to apply an SSM document to. Use `targets` with key `InstanceIds` for document schema versions 2.0 and above.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxConcurrency

The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxErrors

The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify a number, for example 10, or a percentage of the target set, for example 10%.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the SSM document to apply.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameters

A block of arbitrary string parameters to pass to the SSM document.

_Required_: No

_Type_: List of <a href="parameters.md">Parameters</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduleExpression

A cron expression when the association will be applied to the target(s).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutputLocation

_Required_: No

_Type_: List of <a href="outputlocation.md">OutputLocation</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Targets

_Required_: No

_Type_: List of <a href="targets.md">Targets</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AssociationId

Returns the <code>AssociationId</code> value.

#### Id

Returns the <code>Id</code> value.

