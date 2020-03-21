# Terraform::Google::CloudRunService Template Spec

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#containerconcurrency" title="ContainerConcurrency">ContainerConcurrency</a>" : <i>Double</i>,
    "<a href="#serviceaccountname" title="ServiceAccountName">ServiceAccountName</a>" : <i>String</i>,
    "<a href="#containers" title="Containers">Containers</a>" : <i>[ &lt;a href=&#34;template-spec-containers.md&#34;&gt;Containers&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#containerconcurrency" title="ContainerConcurrency">ContainerConcurrency</a>: <i>Double</i>
<a href="#serviceaccountname" title="ServiceAccountName">ServiceAccountName</a>: <i>String</i>
<a href="#containers" title="Containers">Containers</a>: <i>
      - &lt;a href=&#34;template-spec-containers.md&#34;&gt;Containers&lt;/a&gt;</i>
</pre>

## Properties

#### ContainerConcurrency

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccountName

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Containers

_Required_: No
_Type_: List of &lt;a href=&#34;template-spec-containers.md&#34;&gt;Containers&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

