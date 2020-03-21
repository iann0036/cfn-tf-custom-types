# Terraform::AWS::GlueCrawler

CloudFormation equivalent of aws_glue_crawler

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::GlueCrawler",
    "Properties" : {
        "<a href="#classifiers" title="Classifiers">Classifiers</a>" : <i>[ String, ... ]</i>,
        "<a href="#configuration" title="Configuration">Configuration</a>" : <i>String</i>,
        "<a href="#databasename" title="DatabaseName">DatabaseName</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#role" title="Role">Role</a>" : <i>String</i>,
        "<a href="#schedule" title="Schedule">Schedule</a>" : <i>String</i>,
        "<a href="#securityconfiguration" title="SecurityConfiguration">SecurityConfiguration</a>" : <i>String</i>,
        "<a href="#tableprefix" title="TablePrefix">TablePrefix</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#catalogtarget" title="CatalogTarget">CatalogTarget</a>" : <i>[ &lt;a href=&#34;catalogtarget.md&#34;&gt;CatalogTarget&lt;/a&gt;, ... ]</i>,
        "<a href="#dynamodbtarget" title="DynamodbTarget">DynamodbTarget</a>" : <i>[ &lt;a href=&#34;dynamodbtarget.md&#34;&gt;DynamodbTarget&lt;/a&gt;, ... ]</i>,
        "<a href="#jdbctarget" title="JdbcTarget">JdbcTarget</a>" : <i>[ &lt;a href=&#34;jdbctarget.md&#34;&gt;JdbcTarget&lt;/a&gt;, ... ]</i>,
        "<a href="#s3target" title="S3Target">S3Target</a>" : <i>[ &lt;a href=&#34;s3target.md&#34;&gt;S3Target&lt;/a&gt;, ... ]</i>,
        "<a href="#schemachangepolicy" title="SchemaChangePolicy">SchemaChangePolicy</a>" : <i>[ &lt;a href=&#34;schemachangepolicy.md&#34;&gt;SchemaChangePolicy&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::GlueCrawler
Properties:
    <a href="#classifiers" title="Classifiers">Classifiers</a>: <i>
      - String</i>
    <a href="#configuration" title="Configuration">Configuration</a>: <i>String</i>
    <a href="#databasename" title="DatabaseName">DatabaseName</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#role" title="Role">Role</a>: <i>String</i>
    <a href="#schedule" title="Schedule">Schedule</a>: <i>String</i>
    <a href="#securityconfiguration" title="SecurityConfiguration">SecurityConfiguration</a>: <i>String</i>
    <a href="#tableprefix" title="TablePrefix">TablePrefix</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#catalogtarget" title="CatalogTarget">CatalogTarget</a>: <i>
      - &lt;a href=&#34;catalogtarget.md&#34;&gt;CatalogTarget&lt;/a&gt;</i>
    <a href="#dynamodbtarget" title="DynamodbTarget">DynamodbTarget</a>: <i>
      - &lt;a href=&#34;dynamodbtarget.md&#34;&gt;DynamodbTarget&lt;/a&gt;</i>
    <a href="#jdbctarget" title="JdbcTarget">JdbcTarget</a>: <i>
      - &lt;a href=&#34;jdbctarget.md&#34;&gt;JdbcTarget&lt;/a&gt;</i>
    <a href="#s3target" title="S3Target">S3Target</a>: <i>
      - &lt;a href=&#34;s3target.md&#34;&gt;S3Target&lt;/a&gt;</i>
    <a href="#schemachangepolicy" title="SchemaChangePolicy">SchemaChangePolicy</a>: <i>
      - &lt;a href=&#34;schemachangepolicy.md&#34;&gt;SchemaChangePolicy&lt;/a&gt;</i>
</pre>

## Properties

#### Classifiers

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Configuration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityConfiguration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TablePrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CatalogTarget

_Required_: No

_Type_: List of &lt;a href=&#34;catalogtarget.md&#34;&gt;CatalogTarget&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamodbTarget

_Required_: No

_Type_: List of &lt;a href=&#34;dynamodbtarget.md&#34;&gt;DynamodbTarget&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JdbcTarget

_Required_: No

_Type_: List of &lt;a href=&#34;jdbctarget.md&#34;&gt;JdbcTarget&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3Target

_Required_: No

_Type_: List of &lt;a href=&#34;s3target.md&#34;&gt;S3Target&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SchemaChangePolicy

_Required_: No

_Type_: List of &lt;a href=&#34;schemachangepolicy.md&#34;&gt;SchemaChangePolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the &lt;code&gt;Arn&lt;/code&gt; value.

