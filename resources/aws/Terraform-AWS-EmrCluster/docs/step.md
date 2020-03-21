# Terraform::AWS::EmrCluster Step

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#actiononfailure" title="ActionOnFailure">ActionOnFailure</a>" : <i>String</i>,
    "<a href="#hadoopjarstep" title="HadoopJarStep">HadoopJarStep</a>" : <i>[ <a href="step-hadoopjarstep.md">HadoopJarStep</a>, ... ]</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#actiononfailure" title="ActionOnFailure">ActionOnFailure</a>: <i>String</i>
<a href="#hadoopjarstep" title="HadoopJarStep">HadoopJarStep</a>: <i>
      - <a href="step-hadoopjarstep.md">HadoopJarStep</a></i>
<a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### ActionOnFailure

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HadoopJarStep

_Required_: No

_Type_: List of <a href="step-hadoopjarstep.md">HadoopJarStep</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

