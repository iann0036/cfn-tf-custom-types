# TF::AzureRM::DataFactoryLinkedServiceAzureDatabricks NewClusterConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#clusterversion" title="ClusterVersion">ClusterVersion</a>" : <i>String</i>,
    "<a href="#customtags" title="CustomTags">CustomTags</a>" : <i>[ <a href="customtagsdefinition.md">CustomTagsDefinition</a>, ... ]</i>,
    "<a href="#drivernodetype" title="DriverNodeType">DriverNodeType</a>" : <i>String</i>,
    "<a href="#initscripts" title="InitScripts">InitScripts</a>" : <i>[ String, ... ]</i>,
    "<a href="#logdestination" title="LogDestination">LogDestination</a>" : <i>String</i>,
    "<a href="#maxnumberofworkers" title="MaxNumberOfWorkers">MaxNumberOfWorkers</a>" : <i>Double</i>,
    "<a href="#minnumberofworkers" title="MinNumberOfWorkers">MinNumberOfWorkers</a>" : <i>Double</i>,
    "<a href="#nodetype" title="NodeType">NodeType</a>" : <i>String</i>,
    "<a href="#sparkconfig" title="SparkConfig">SparkConfig</a>" : <i>[ <a href="sparkconfigdefinition.md">SparkConfigDefinition</a>, ... ]</i>,
    "<a href="#sparkenvironmentvariables" title="SparkEnvironmentVariables">SparkEnvironmentVariables</a>" : <i>[ <a href="sparkenvironmentvariablesdefinition.md">SparkEnvironmentVariablesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#clusterversion" title="ClusterVersion">ClusterVersion</a>: <i>String</i>
<a href="#customtags" title="CustomTags">CustomTags</a>: <i>
      - <a href="customtagsdefinition.md">CustomTagsDefinition</a></i>
<a href="#drivernodetype" title="DriverNodeType">DriverNodeType</a>: <i>String</i>
<a href="#initscripts" title="InitScripts">InitScripts</a>: <i>
      - String</i>
<a href="#logdestination" title="LogDestination">LogDestination</a>: <i>String</i>
<a href="#maxnumberofworkers" title="MaxNumberOfWorkers">MaxNumberOfWorkers</a>: <i>Double</i>
<a href="#minnumberofworkers" title="MinNumberOfWorkers">MinNumberOfWorkers</a>: <i>Double</i>
<a href="#nodetype" title="NodeType">NodeType</a>: <i>String</i>
<a href="#sparkconfig" title="SparkConfig">SparkConfig</a>: <i>
      - <a href="sparkconfigdefinition.md">SparkConfigDefinition</a></i>
<a href="#sparkenvironmentvariables" title="SparkEnvironmentVariables">SparkEnvironmentVariables</a>: <i>
      - <a href="sparkenvironmentvariablesdefinition.md">SparkEnvironmentVariablesDefinition</a></i>
</pre>

## Properties

#### ClusterVersion

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomTags

_Required_: No

_Type_: List of <a href="customtagsdefinition.md">CustomTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DriverNodeType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitScripts

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogDestination

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxNumberOfWorkers

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinNumberOfWorkers

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SparkConfig

_Required_: No

_Type_: List of <a href="sparkconfigdefinition.md">SparkConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SparkEnvironmentVariables

_Required_: No

_Type_: List of <a href="sparkenvironmentvariablesdefinition.md">SparkEnvironmentVariablesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

