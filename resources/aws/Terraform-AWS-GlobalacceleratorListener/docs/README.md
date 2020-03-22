# Terraform::AWS::GlobalacceleratorListener

CloudFormation equivalent of aws_globalaccelerator_listener

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::GlobalacceleratorListener",
    "Properties" : {
        "<a href="#acceleratorarn" title="AcceleratorArn">AcceleratorArn</a>" : <i>String</i>,
        "<a href="#clientaffinity" title="ClientAffinity">ClientAffinity</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#portrange" title="PortRange">PortRange</a>" : <i>[ <a href="portrange.md">PortRange</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::GlobalacceleratorListener
Properties:
    <a href="#acceleratorarn" title="AcceleratorArn">AcceleratorArn</a>: <i>String</i>
    <a href="#clientaffinity" title="ClientAffinity">ClientAffinity</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#portrange" title="PortRange">PortRange</a>: <i>
      - <a href="portrange.md">PortRange</a></i>
</pre>

## Properties

#### AcceleratorArn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientAffinity

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortRange

_Required_: No

_Type_: List of <a href="portrange.md">PortRange</a>

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

