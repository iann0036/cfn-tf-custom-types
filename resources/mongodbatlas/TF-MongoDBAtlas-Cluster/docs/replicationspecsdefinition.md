# TF::MongoDBAtlas::Cluster ReplicationSpecsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#numshards" title="NumShards">NumShards</a>" : <i>Double</i>,
    "<a href="#zonename" title="ZoneName">ZoneName</a>" : <i>String</i>,
    "<a href="#regionsconfig" title="RegionsConfig">RegionsConfig</a>" : <i>[ <a href="regionsconfigdefinition.md">RegionsConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#numshards" title="NumShards">NumShards</a>: <i>Double</i>
<a href="#zonename" title="ZoneName">ZoneName</a>: <i>String</i>
<a href="#regionsconfig" title="RegionsConfig">RegionsConfig</a>: <i>
      - <a href="regionsconfigdefinition.md">RegionsConfigDefinition</a></i>
</pre>

## Properties

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumShards

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegionsConfig

_Required_: No

_Type_: List of <a href="regionsconfigdefinition.md">RegionsConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

