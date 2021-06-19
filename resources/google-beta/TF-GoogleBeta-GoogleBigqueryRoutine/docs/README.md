# TF::GoogleBeta::GoogleBigqueryRoutine

CloudFormation equivalent of google_bigquery_routine

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GoogleBeta::GoogleBigqueryRoutine",
    "Properties" : {
        "<a href="#datasetid" title="DatasetId">DatasetId</a>" : <i>String</i>,
        "<a href="#definitionbody" title="DefinitionBody">DefinitionBody</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#determinismlevel" title="DeterminismLevel">DeterminismLevel</a>" : <i>String</i>,
        "<a href="#importedlibraries" title="ImportedLibraries">ImportedLibraries</a>" : <i>[ String, ... ]</i>,
        "<a href="#language" title="Language">Language</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#returntype" title="ReturnType">ReturnType</a>" : <i>String</i>,
        "<a href="#routineid" title="RoutineId">RoutineId</a>" : <i>String</i>,
        "<a href="#routinetype" title="RoutineType">RoutineType</a>" : <i>String</i>,
        "<a href="#arguments" title="Arguments">Arguments</a>" : <i>[ <a href="argumentsdefinition.md">ArgumentsDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GoogleBeta::GoogleBigqueryRoutine
Properties:
    <a href="#datasetid" title="DatasetId">DatasetId</a>: <i>String</i>
    <a href="#definitionbody" title="DefinitionBody">DefinitionBody</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#determinismlevel" title="DeterminismLevel">DeterminismLevel</a>: <i>String</i>
    <a href="#importedlibraries" title="ImportedLibraries">ImportedLibraries</a>: <i>
      - String</i>
    <a href="#language" title="Language">Language</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#returntype" title="ReturnType">ReturnType</a>: <i>String</i>
    <a href="#routineid" title="RoutineId">RoutineId</a>: <i>String</i>
    <a href="#routinetype" title="RoutineType">RoutineType</a>: <i>String</i>
    <a href="#arguments" title="Arguments">Arguments</a>: <i>
      - <a href="argumentsdefinition.md">ArgumentsDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### DatasetId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinitionBody

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeterminismLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImportedLibraries

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Language

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReturnType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoutineId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoutineType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Arguments

_Required_: No

_Type_: List of <a href="argumentsdefinition.md">ArgumentsDefinition</a>

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

#### CreationTime

Returns the <code>CreationTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### LastModifiedTime

Returns the <code>LastModifiedTime</code> value.

