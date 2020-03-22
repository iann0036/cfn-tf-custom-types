# Terraform::OpenTelekomCloud::MrsJobV1

Manages resource job within OpenTelekomCloud MRS.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenTelekomCloud::MrsJobV1",
    "Properties" : {
        "<a href="#arguments" title="Arguments">Arguments</a>" : <i>String</i>,
        "<a href="#clusterid" title="ClusterId">ClusterId</a>" : <i>String</i>,
        "<a href="#hivescriptpath" title="HiveScriptPath">HiveScriptPath</a>" : <i>String</i>,
        "<a href="#input" title="Input">Input</a>" : <i>String</i>,
        "<a href="#isprotected" title="IsProtected">IsProtected</a>" : <i>Boolean</i>,
        "<a href="#ispublic" title="IsPublic">IsPublic</a>" : <i>Boolean</i>,
        "<a href="#jarpath" title="JarPath">JarPath</a>" : <i>String</i>,
        "<a href="#joblog" title="JobLog">JobLog</a>" : <i>String</i>,
        "<a href="#jobname" title="JobName">JobName</a>" : <i>String</i>,
        "<a href="#jobtype" title="JobType">JobType</a>" : <i>Double</i>,
        "<a href="#output" title="Output">Output</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenTelekomCloud::MrsJobV1
Properties:
    <a href="#arguments" title="Arguments">Arguments</a>: <i>String</i>
    <a href="#clusterid" title="ClusterId">ClusterId</a>: <i>String</i>
    <a href="#hivescriptpath" title="HiveScriptPath">HiveScriptPath</a>: <i>String</i>
    <a href="#input" title="Input">Input</a>: <i>String</i>
    <a href="#isprotected" title="IsProtected">IsProtected</a>: <i>Boolean</i>
    <a href="#ispublic" title="IsPublic">IsPublic</a>: <i>Boolean</i>
    <a href="#jarpath" title="JarPath">JarPath</a>: <i>String</i>
    <a href="#joblog" title="JobLog">JobLog</a>: <i>String</i>
    <a href="#jobname" title="JobName">JobName</a>: <i>String</i>
    <a href="#jobtype" title="JobType">JobType</a>: <i>Double</i>
    <a href="#output" title="Output">Output</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Arguments

Key parameter for program execution. The parameter
is specified by the function of the user's program. MRS is only responsible
for loading the parameter. The parameter contains a maximum of 2047 characters,
excluding special characters such as ;|&>'<$, and can be empty.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterId

Cluster ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HiveScriptPath

SQL program path This parameter is needed
by Spark Script and Hive Script jobs only and must meet the following requirements:
Contains a maximum of 1023 characters, excluding special characters such as
;|&><'$. The address cannot be empty or full of spaces. Starts with / or s3a://.
Ends with .sql. sql is case-insensitive.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Input

Path for inputting data, which must start with / or s3a://.
A correct OBS path is required. The parameter contains a maximum of 1023 characters,
excluding special characters such as ;|&>'<$, and can be empty.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsProtected

Whether a job is protected true false The current
version does not support this function.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsPublic

Whether a job is public true false The current version
does not support this function.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JarPath

Path of the .jar package or .sql file for program
execution The parameter must meet the following requirements: Contains a maximum
of 1023 characters, excluding special characters such as ;|&><'$. The address
cannot be empty or full of spaces. Starts with / or s3a://. Spark Script must
end with .sql; while MapReduce and Spark Jar must end with .jar. sql and jar
are case-insensitive.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JobLog

Path for storing job logs that record job running status.
This path must start with / or s3a://. A correct OBS path is required. The parameter
contains a maximum of 1023 characters, excluding special characters such as
;|&>'<$, and can be empty.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JobName

Job name Contains only 1 to 64 letters, digits, hyphens
(-), and underscores (_). NOTE: Identical job names are allowed but not recommended.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JobType

Job type 1: MapReduce 2: Spark 3: Hive Script 4: HiveQL
(not supported currently) 5: DistCp, importing and exporting data.  6: Spark
Script 7: Spark SQL, submitting Spark SQL statements. (not supported in this
APIcurrently) NOTE: Spark and Hive jobs can be added to only clusters including
Spark and Hive components.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Output

Path for outputting data, which must start with / or
s3a://. A correct OBS path is required. If the path does not exist, the system
automatically creates it. The parameter contains a maximum of 1023 characters,
excluding special characters such as ;|&>'<$, and can be empty.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### JobState

Returns the <code>JobState</code> value.

