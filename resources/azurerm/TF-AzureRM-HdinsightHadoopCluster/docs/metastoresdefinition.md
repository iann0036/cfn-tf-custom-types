# TF::AzureRM::HdinsightHadoopCluster MetastoresDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ambari" title="Ambari">Ambari</a>" : <i>[ <a href="ambaridefinition.md">AmbariDefinition</a>, ... ]</i>,
    "<a href="#hive" title="Hive">Hive</a>" : <i>[ <a href="hivedefinition.md">HiveDefinition</a>, ... ]</i>,
    "<a href="#oozie" title="Oozie">Oozie</a>" : <i>[ <a href="ooziedefinition.md">OozieDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ambari" title="Ambari">Ambari</a>: <i>
      - <a href="ambaridefinition.md">AmbariDefinition</a></i>
<a href="#hive" title="Hive">Hive</a>: <i>
      - <a href="hivedefinition.md">HiveDefinition</a></i>
<a href="#oozie" title="Oozie">Oozie</a>: <i>
      - <a href="ooziedefinition.md">OozieDefinition</a></i>
</pre>

## Properties

#### Ambari

_Required_: No

_Type_: List of <a href="ambaridefinition.md">AmbariDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hive

_Required_: No

_Type_: List of <a href="hivedefinition.md">HiveDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Oozie

_Required_: No

_Type_: List of <a href="ooziedefinition.md">OozieDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

