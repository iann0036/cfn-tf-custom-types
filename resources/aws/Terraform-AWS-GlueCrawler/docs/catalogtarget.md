# Terraform::AWS::GlueCrawler CatalogTarget

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#databasename" title="DatabaseName">DatabaseName</a>" : <i>String</i>,
    "<a href="#tables" title="Tables">Tables</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#databasename" title="DatabaseName">DatabaseName</a>: <i>String</i>
<a href="#tables" title="Tables">Tables</a>: <i>
      - String</i>
</pre>

## Properties

#### DatabaseName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tables

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

