# Terraform::AWS::CodecommitTrigger

CloudFormation equivalent of aws_codecommit_trigger

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::CodecommitTrigger",
    "Properties" : {
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#repositoryname" title="RepositoryName">RepositoryName</a>" : <i>String</i>,
        "<a href="#trigger" title="Trigger">Trigger</a>" : <i>[ &lt;a href=&#34;trigger.md&#34;&gt;Trigger&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::CodecommitTrigger
Properties:
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#repositoryname" title="RepositoryName">RepositoryName</a>: <i>String</i>
    <a href="#trigger" title="Trigger">Trigger</a>: <i>
      - &lt;a href=&#34;trigger.md&#34;&gt;Trigger&lt;/a&gt;</i>
</pre>

## Properties

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RepositoryName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trigger

_Required_: No

_Type_: List of &lt;a href=&#34;trigger.md&#34;&gt;Trigger&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ConfigurationId

Returns the &lt;code&gt;ConfigurationId&lt;/code&gt; value.

