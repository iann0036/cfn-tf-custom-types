# TF::Kubernetes::CsiDriver SpecDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#attachrequired" title="AttachRequired">AttachRequired</a>" : <i>Boolean</i>,
    "<a href="#podinfoonmount" title="PodInfoOnMount">PodInfoOnMount</a>" : <i>Boolean</i>,
    "<a href="#volumelifecyclemodes" title="VolumeLifecycleModes">VolumeLifecycleModes</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#attachrequired" title="AttachRequired">AttachRequired</a>: <i>Boolean</i>
<a href="#podinfoonmount" title="PodInfoOnMount">PodInfoOnMount</a>: <i>Boolean</i>
<a href="#volumelifecyclemodes" title="VolumeLifecycleModes">VolumeLifecycleModes</a>: <i>
      - String</i>
</pre>

## Properties

#### AttachRequired

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PodInfoOnMount

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeLifecycleModes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

