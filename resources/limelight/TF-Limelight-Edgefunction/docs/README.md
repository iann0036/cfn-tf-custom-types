# TF::Limelight::Edgefunction

This resource provides a way to manage EdgeFunctions in Limelight Networks.
For more details see the [API docs](https://support.limelight.com/public/openapi/edgefunctions/index.html#tag/Function-Management)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Limelight::Edgefunction",
    "Properties" : {
        "<a href="#candebug" title="CanDebug">CanDebug</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#functionarchive" title="FunctionArchive">FunctionArchive</a>" : <i>String</i>,
        "<a href="#functionsha256" title="FunctionSha256">FunctionSha256</a>" : <i>String</i>,
        "<a href="#handler" title="Handler">Handler</a>" : <i>String</i>,
        "<a href="#memory" title="Memory">Memory</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#reservedconcurrency" title="ReservedConcurrency">ReservedConcurrency</a>" : <i>Double</i>,
        "<a href="#runtime" title="Runtime">Runtime</a>" : <i>String</i>,
        "<a href="#shortname" title="Shortname">Shortname</a>" : <i>String</i>,
        "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
        "<a href="#environmentvariable" title="EnvironmentVariable">EnvironmentVariable</a>" : <i>[ <a href="environmentvariabledefinition.md">EnvironmentVariableDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Limelight::Edgefunction
Properties:
    <a href="#candebug" title="CanDebug">CanDebug</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#functionarchive" title="FunctionArchive">FunctionArchive</a>: <i>String</i>
    <a href="#functionsha256" title="FunctionSha256">FunctionSha256</a>: <i>String</i>
    <a href="#handler" title="Handler">Handler</a>: <i>String</i>
    <a href="#memory" title="Memory">Memory</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#reservedconcurrency" title="ReservedConcurrency">ReservedConcurrency</a>: <i>Double</i>
    <a href="#runtime" title="Runtime">Runtime</a>: <i>String</i>
    <a href="#shortname" title="Shortname">Shortname</a>: <i>String</i>
    <a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
    <a href="#environmentvariable" title="EnvironmentVariable">EnvironmentVariable</a>: <i>
      - <a href="environmentvariabledefinition.md">EnvironmentVariableDefinition</a></i>
</pre>

## Properties

#### CanDebug

Boolean flag to enable debug IO. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A description for the EdgeFunction.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FunctionArchive

Path to the function archive (zip file).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FunctionSha256

The SHA256 value of the `function_archive`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Handler

Handler that's run when the EdgeFunction is invoked.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Memory

The memory allocated to the EdgeFunction. Defaults to `256`. CPU is allocated
proportional to memory.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The environment variable name.
* `value` - (Required) The environment variable value.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReservedConcurrency

Sets the reserved concurrency for the EdgeFunction. Defaults to `0`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Runtime

The runtime for the EdgeFunction.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shortname

The account name (shortname).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

Timeout for the EdgeFunction execution in milliseconds. Defaults to `5000`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvironmentVariable

_Required_: No

_Type_: List of <a href="environmentvariabledefinition.md">EnvironmentVariableDefinition</a>

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

#### RevisionId

Returns the <code>RevisionId</code> value.

