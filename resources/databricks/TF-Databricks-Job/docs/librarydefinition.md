# TF::Databricks::Job LibraryDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#egg" title="Egg">Egg</a>" : <i>String</i>,
    "<a href="#jar" title="Jar">Jar</a>" : <i>String</i>,
    "<a href="#whl" title="Whl">Whl</a>" : <i>String</i>,
    "<a href="#cran" title="Cran">Cran</a>" : <i>[ <a href="crandefinition.md">CranDefinition</a>, ... ]</i>,
    "<a href="#maven" title="Maven">Maven</a>" : <i>[ <a href="mavendefinition.md">MavenDefinition</a>, ... ]</i>,
    "<a href="#pypi" title="Pypi">Pypi</a>" : <i>[ <a href="pypidefinition.md">PypiDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#egg" title="Egg">Egg</a>: <i>String</i>
<a href="#jar" title="Jar">Jar</a>: <i>String</i>
<a href="#whl" title="Whl">Whl</a>: <i>String</i>
<a href="#cran" title="Cran">Cran</a>: <i>
      - <a href="crandefinition.md">CranDefinition</a></i>
<a href="#maven" title="Maven">Maven</a>: <i>
      - <a href="mavendefinition.md">MavenDefinition</a></i>
<a href="#pypi" title="Pypi">Pypi</a>: <i>
      - <a href="pypidefinition.md">PypiDefinition</a></i>
</pre>

## Properties

#### Egg

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Jar

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Whl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cran

_Required_: No

_Type_: List of <a href="crandefinition.md">CranDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Maven

_Required_: No

_Type_: List of <a href="mavendefinition.md">MavenDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pypi

_Required_: No

_Type_: List of <a href="pypidefinition.md">PypiDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

