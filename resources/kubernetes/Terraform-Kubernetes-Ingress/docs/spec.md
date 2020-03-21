# Terraform::Kubernetes::Ingress Spec

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#backend" title="Backend">Backend</a>" : <i>[ <a href="spec-backend.md">Backend</a>, ... ]</i>,
    "<a href="#rule" title="Rule">Rule</a>" : <i>[ <a href="spec-rule.md">Rule</a>, ... ]</i>,
    "<a href="#tls" title="Tls">Tls</a>" : <i>[ <a href="spec-tls.md">Tls</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#backend" title="Backend">Backend</a>: <i>
      - <a href="spec-backend.md">Backend</a></i>
<a href="#rule" title="Rule">Rule</a>: <i>
      - <a href="spec-rule.md">Rule</a></i>
<a href="#tls" title="Tls">Tls</a>: <i>
      - <a href="spec-tls.md">Tls</a></i>
</pre>

## Properties

#### Backend

_Required_: No
_Type_: List of <a href="spec-backend.md">Backend</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: No
_Type_: List of <a href="spec-rule.md">Rule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tls

_Required_: No
_Type_: List of <a href="spec-tls.md">Tls</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

